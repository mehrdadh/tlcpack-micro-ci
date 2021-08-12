import argparse
import subprocess
import logging as _LOG
import re
import os
import enum
import json
from tabulate import tabulate
import logging

MICROTVM_PLATFORM_INFO = {
    "nrf5340dk": {"manufacturer": "SEGGER", "vid_hex": "1366", "pid_hex": "1055"},
    "stm32f746xx_nucleo": {
        "manufacturer": "STMicroelectronics",
        "vid_hex": "0483",
        "pid_hex": "374b",
    },
    "stm32f746xx_disco": {
        "manufacturer": "STMicroelectronics",
        "vid_hex": "0483",
        "pid_hex": "374b",
    },
    "stm32l4r5zi_nucleo": {
        "manufacturer": "STMicroelectronics",
        "vid_hex": "0483",
        "pid_hex": "374b",
    },
}

VIRTUALBOX_VID_PID_RE = re.compile(r"0x([0-9A-Fa-f]{4}).*")

DEVICE_TABLE_FILE = os.path.join(
    subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"], encoding="utf-8"
    ).strip(),
    "config",
    "device_table.json",
)

LOG_ = logging.getLogger()


class MicroDevice(object):
    """A microTVM device instance."""

    def __init__(self, type: str, serial_number: str) -> None:
        """
        Parameters
        ----------
        _type : str
            Device type.
        _serial_number : str
            Device serial number.
        _taken : bool
            If device is aquired.
        _user : str
            Username who aquired this device.
        _enabled : bool
            True if device is enabled to use.
        """
        self._type = type
        self._serial_number = serial_number
        self._is_taken = False
        self._user = None
        self._enabled = True
        super().__init__()

    def GetSerialNumber(self) -> str:
        return self._serial_number

    def GetType(self) -> str:
        return self._type

    def SetSerialNumber(self, serial_number: str):
        self._serial_number = serial_number

    def SetTaken(self):
        self._is_taken = True

    def SetUser(self, user=None):
        if not user:
            self._user = "Unknown"
        else:
            self._user = user
        self.SetTaken()

    def Enable(self, status: str):
        self._enabled = status

    def Free(self):
        self._is_taken = False
        self._user = None


class GRPCSessionTasks(str, enum.Enum):
    SESSION_CLOSE = "session_close"
    SESSION_CLOSED = "session_closed"


class MicroTVMPlatforms:
    """An instance to keep all MicroDevice devices"""

    def __init__(self):
        """
        Parameters
        ----------
        _platforms : list[MicroDevice]
            List of MicroDevices.
        _serial_numbers : set[str]
            Set of serial numbers of all MicroDevices.
        _sessions : dict[str]
            A dictionary that keeps MicroDevices for each connected session.
        """
        self._platforms = list()
        self._serial_numbers = set()
        self._sessions = dict()

    def __str__(self):
        headers = ["#", "Type", "Serial", "Available", "User", "Enabled"]
        data = []
        for device in self._platforms:
            data.append(
                [
                    device.GetType(),
                    device.GetSerialNumber(),
                    not device._is_taken,
                    str(device._user),
                    device._enabled,
                ]
            )
        data = sorted(data, key=lambda l:l[0].lower(), reverse=False)
        message = "\n"
        message += str(tabulate(data, headers=headers, showindex='always'))
        return message

    def AddPlatform(self, device: MicroDevice):
        if device.GetSerialNumber() not in self._serial_numbers:
            self._serial_numbers.add(device.GetSerialNumber())
            self._platforms.append(device)

    def GetType(self, serial_number: str) -> str:
        for platform in self._platforms:
            if platform._serial_number == serial_number:
                return platform._type

    def GetPlatform(self, type: str, session_number: str, username: str) -> str:
        for platform in self._platforms:
            if platform._type == type and not platform._is_taken and platform._enabled:
                platform._is_taken = True
                platform._user = username
                serial_number = platform.GetSerialNumber()
                self._sessions[session_number].append(serial_number)
                return serial_number
        return ""

    def ReleasePlatform(self, serial_number: str):
        for platform in self._platforms:
            if platform.GetSerialNumber() == serial_number:
                platform.Free()
                return
        LOG_.warning(f"SerialNumber {serial_number} was not found.")

    def EnablePlatform(self, serial_number: str, status: bool)-> bool:
        for platform in self._platforms:
            if platform.GetSerialNumber() == serial_number:
                platform.Enable(status)
                return True
        return False

def LoadDeviceTable(table_file: str) -> MicroTVMPlatforms:
    """Load device table Json file to MicroTVMPlatforms."""
    with open(table_file, "r") as json_f:
        data = json.load(json_f)
        device_table = MicroTVMPlatforms()
        for device_type, config in data.items():
            for item in config["instances"]:
                new_device = MicroDevice(type=device_type, serial_number=item)
                device_table.AddPlatform(new_device)
    return device_table


def GetAllDeviceTypes() -> set():
    """Generates all device types that are available on this hardware node."""
    device_table = LoadDeviceTable(DEVICE_TABLE_FILE)
    device_types = set()
    for device in device_table._platforms:
        device_types.add(device.GetType())
    return device_types


def ParseVirtualBoxDevices(microtvm_platform: str) -> list:
    """Parse usb devices and return a list of devices maching microtvm_platform."""

    output = subprocess.check_output(
        ["VBoxManage", "list", "usbhost"], encoding="utf-8"
    )
    devices = []
    current_dev = {}
    for line in output.split("\n"):
        if not line.strip():
            if current_dev:
                if "VendorId" in current_dev and "ProductId" in current_dev:
                    # Update VendorId and ProductId to hex
                    m = VIRTUALBOX_VID_PID_RE.match(current_dev["VendorId"])
                    if not m:
                        _LOG.warning("Malformed VendorId: %s", current_dev["VendorId"])
                        current_dev = {}
                        continue

                    m = VIRTUALBOX_VID_PID_RE.match(current_dev["ProductId"])
                    if not m:
                        _LOG.warning(
                            "Malformed ProductId: %s", current_dev["ProductId"]
                        )
                        current_dev = {}
                        continue

                    current_dev["vid_hex"] = (
                        current_dev["VendorId"]
                        .replace("(", "")
                        .replace(")", "")
                        .split(" ")[1]
                        .lower()
                    )
                    current_dev.pop("VendorId", None)

                    current_dev["pid_hex"] = (
                        current_dev["ProductId"]
                        .replace("(", "")
                        .replace(")", "")
                        .split(" ")[1]
                        .lower()
                    )
                    current_dev.pop("ProductId", None)

                    if (
                        current_dev["vid_hex"]
                        == MICROTVM_PLATFORM_INFO[microtvm_platform]["vid_hex"]
                        and current_dev["pid_hex"]
                        == MICROTVM_PLATFORM_INFO[microtvm_platform]["pid_hex"]
                    ):
                        devices.append(current_dev)
                current_dev = {}

            continue

        key, value = line.split(":", 1)
        value = value.lstrip(" ")
        current_dev[key] = value

    if current_dev:
        devices.append(current_dev)
    return devices


def ListConnectedDevices(microtvm_platform: str) -> list:
    """List all platforms connected to this hardware node."""

    devices = ParseVirtualBoxDevices(microtvm_platform)
    device_list = []
    for device in devices:
        device_list.append(
            {
                "SerialNumber": device["SerialNumber"],
                "UUID": device["UUID"],
                "State": device["Current State"],
            }
        )
    return device_list


def DeviceIsAlive(platform: str, serial: str) -> bool:
    devices = ListConnectedDevices(platform)
    for device in devices:
        if device["SerialNumber"] == serial:
            return True
    return False


def command_list(args: argparse.Namespace):
    """Print connected MicroTVM devices."""

    devices = ListConnectedDevices(args.microtvm_platform)
    results = ""
    for device in devices:
        results += f"SerialNumber:{device['SerialNumber']}\tUUID: {device['UUID']}\tState:{device['State']}\n"
    print(results)


def VirtualBoxGetInfo(machine_uuid: str) -> dict:
    """
    Get virtual box information and return as a dictionary.
    """
    output = subprocess.check_output(
        ["vboxmanage", "showvminfo", machine_uuid], encoding="utf-8"
    )
    machine_info = {}
    for line in output.split("\n"):
        _LOG.debug(line)
        try:
            key, value = line.split(":", 1)
            value = value.lstrip(" ")
            # To capture multiple microTVM devices
            if key in machine_info:
                if machine_info[key] is list:
                    machine_info[key].append(value)
                else:
                    machine_info[key] = [machine_info[key], value]
            else:
                machine_info[key] = value
        except:
            continue
    _LOG.debug(f"machine info:\n{machine_info}")
    return machine_info


def virtualbox_is_live(machine_uuid: str):
    """
    Return True if this virtualbox is running
    """
    machine_info = VirtualBoxGetInfo(machine_uuid)
    if "running" in machine_info["State"]:
        return True
    return False


def attach_command(args):
    attach(args.microtvm_platform, args.vm_path, args.serial)


def attach(microtvm_platfrom: str, vm_path: str, serial_number: str):
    """
    Attach a microTVM platform to a virtualbox.
    """
    usb_devices = ParseVirtualBoxDevices(microtvm_platfrom)
    found = False
    for dev in usb_devices:
        if dev["SerialNumber"] == serial_number:
            vid_hex = dev["vid_hex"]
            pid_hex = dev["pid_hex"]
            serial = dev["SerialNumber"]
            dev_uuid = dev["UUID"]
            found = True
            break

    if not found:
        LOG_.warning(f"Device list:\n{usb_devices}")
        raise ValueError(f"Device S/N {serial_number} not found.")

    with open(
        os.path.join(vm_path, ".vagrant", "machines", "default", "virtualbox", "id")
    ) as f:
        machine_uuid = f.read()

    if serial and dev_uuid:
        rule_args = [
            "VBoxManage",
            "usbfilter",
            "add",
            "0",
            "--action",
            "hold",
            "--name",
            "test device",
            "--target",
            machine_uuid,
            "--vendorid",
            vid_hex,
            "--productid",
            pid_hex,
            "--serialnumber",
            serial,
        ]

        # Check if already attached
        machine_info = VirtualBoxGetInfo(machine_uuid)
        if "SerialNumber" in machine_info:
            if serial in machine_info["SerialNumber"]:
                _LOG.info(f"Device {serial} already attached.")
                return

        # if virtualbox_is_live(machine_uuid):
        #     raise RuntimeError("VM is running.")

        # subprocess.check_call(rule_args)
        subprocess.check_call(
            ["VBoxManage", "controlvm", machine_uuid, "usbattach", dev_uuid]
        )
        _LOG.info(f"USB with S/N {serial} attached.")
        return
    else:
        raise Exception(
            f"Device with vid={vid_hex}, pid={pid_hex}, serial={serial!r} not found:\n{usb_devices!r}"
        )


def detach(microtvm_platfrom: str, vm_path: str, serial_number: str):
    with open(
        os.path.join(vm_path, ".vagrant", "machines", "default", "virtualbox", "id")
    ) as f:
        machine_uuid = f.read()

    usb_devices = ParseVirtualBoxDevices(microtvm_platfrom)
    found = False
    for dev in usb_devices:
        if dev["SerialNumber"] == serial_number:
            vid_hex = dev["vid_hex"]
            pid_hex = dev["pid_hex"]
            serial = dev["SerialNumber"]
            dev_uuid = dev["UUID"]
            found = True
            break
    if not found:
        LOG_.warning(f"Serial {serial_number} not found in usb devies.")
        LOG_.warning(usb_devices)
        return
    subprocess.check_call(
        ["VBoxManage", "controlvm", machine_uuid, "usbdetach", dev_uuid]
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="Action to perform.")

    parser_list = subparsers.add_parser(
        "list", help="List connected devices for a target."
    )
    parser_list.set_defaults(func=command_list)

    parser_attach = subparsers.add_parser(
        "attach", help="Attach a microTVM device to a virtual machine."
    )
    parser_attach.set_defaults(func=attach_command)

    parser_attach.add_argument("--serial", help="microTVM targer serial number.")
    parser_attach.add_argument("--vm-path", help="Location of virtual machine.")

    parser.add_argument(
        "--microtvm-platform",
        required=True,
        choices=GetAllDeviceTypes(),
        help=("microTVM target platform for list."),
    )

    parser.add_argument("--log-level", default=None, help="Log level.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.log_level:
        _LOG.basicConfig(level=args.log_level)
    else:
        _LOG.basicConfig(level="INFO")

    args.func(args)
