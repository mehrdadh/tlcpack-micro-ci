# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import pathlib
from .device_server import LOG_
import grpc
import logging
import argparse
import time
import getpass

from . import microDevice_pb2_grpc
from . import microDevice_pb2
from .device_utils import MicroDevice
from .device_utils import GRPCSessionTasks
from . import device_utils

LOG_ = logging.getLogger("MicroTVM Device Client")


def get_artifact_filename(device: str) -> str:
    return f"serial_{device}.micro"


LOG_ = logging.getLogger("MicroTVM Device Client")


def get_artifact_filename(device: str) -> str:
    return f"serial_{device}.micro"


def test():
    print("mehrdad")


class GRPCMicroDevice:
    _device: MicroDevice = None
    _rpc_stub = None
    _rpc_channel = None
    _session_number: str = None

    def __init__(self, rpc_port: int, device_type: str):
        self._rpc_channel = grpc.insecure_channel(f"localhost:{rpc_port}")
        # self._rpc_channel.subscribe(test())
        self._rpc_stub = microDevice_pb2_grpc.RPCRequestStub(self._rpc_channel)
        self._device = MicroDevice(type=device_type, serial_number="")

        # Request session number
        response = self._rpc_stub.RPCSessionRequest(
            microDevice_pb2.SessionMessage(session_number=None)
        )
        self._session_number = response.session_number

    def RequestDevice(self):
        if not self._device.GetSerialNumber():
            device_type = self._device.GetType()
            response = self._rpc_stub.RPCDeviceRequest(
                microDevice_pb2.DeviceMessage(
                    type=device_type,
                    session_number=self._session_number,
                    user=getpass.getuser(),
                )
            )
            if response.serial_number != "":
                self._device.SetSerialNumber(response.serial_number)

    def ReleaseDevice(self):
        serial_number = self._device.GetSerialNumber()
        assert serial_number, "Serial number not valid."
        device_type = self._device.GetType()
        self._rpc_stub.RPCDeviceRelease(
            microDevice_pb2.DeviceMessage(type=device_type, serial_number=serial_number)
        )

    def IsAlive(self) -> bool:
        response = self._rpc_stub.RPCDeviceIsAlive(
            microDevice_pb2.DeviceMessage(
                type=self._device.GetType(),
                serial_number=self._device.GetSerialNumber(),
            )
        )
        return response.is_alive

    def Close(self):
        self._rpc_stub.RPCSessionClose(
            microDevice_pb2.SessionMessage(
                session_number=self._session_number,
                task=GRPCSessionTasks.SESSION_CLOSE.value,
            )
        )
        self._rpc_channel.close()

    def RequestList(self):
        request = self._rpc_stub.RPCDeviceRequestList(
            microDevice_pb2.StringMessage()
        )
        return request.text

    def EnableDevice(self, serial_number: str, status: bool):
        if status:
            request = self._rpc_stub.RPCDeviceRequestEnable(
                microDevice_pb2.DeviceMessage(serial_number=serial_number)
            )
        else:
            request = self._rpc_stub.RPCDeviceRequestDisable(
                microDevice_pb2.DeviceMessage(serial_number=serial_number)
            )
        print(request.text)

def server_request_device(args: argparse.Namespace) -> str:
    grpc_device = GRPCMicroDevice(args.port, args.device)
    grpc_device.RequestDevice()
    return grpc_device._device.GetSerialNumber()


def server_release_device(serial_number, args):
    grpc_device = GRPCMicroDevice(args.port, args.device)
    grpc_device._device.SetSerialNumber(serial_number)
    grpc_device.ReleaseDevice()


def attach_device(args: argparse.Namespace):
    assert args.vm_path, "Error: Reference VM path missing."

    serial_number = server_request_device(args)
    if not serial_number:
        if args.wait:
            LOG_.info(f"Waiting for {args.device} device...")
            while not serial_number:
                serial_number = server_request_device(args)
                time.sleep(5)
        else:
            return

    try:
        device_utils.attach(args.device, args.vm_path, serial_number)
    except Exception as ex:
        server_release_device(serial_number, args)
        raise RuntimeError(ex)

    if args.artifact_path:
        artifact_file = args.artifact_path / get_artifact_filename(args.device)
        if artifact_file.is_file():
            artifact_file.unlink()
        args.artifact_path.mkdir(parents=True, exist_ok=True)
        with open(artifact_file, "w") as f:
            f.write(str(serial_number))
    LOG_.info(f"Device {serial_number} attached.")


def detach_device(args: argparse.Namespace):
    # Release USB device from the RVM
    if args.artifact_path:
        artifact_file = args.artifact_path / get_artifact_filename(args.device)
        with open(artifact_file, "r") as f:
            serial_number = f.read()
    else:
        serial_number = args.serial

    device_utils.detach(args.device, args.vm_path, serial_number)
    # Release device from the microTVM device server
    server_release_device(serial_number, args)


def request_device(args: argparse.Namespace):
    serial_number = server_request_device(args)
    if not serial_number:
        if args.wait:
            LOG_.info(f"Waiting for {args.device} device...")
            while not serial_number:
                serial_number = server_request_device(args)
                time.sleep(5)
    return serial_number


def release_device(args: argparse.Namespace):
    server_release_device(args.serial, args)


def request_device(args: argparse.Namespace):
    serial_number = server_request_device(args)
    if not serial_number:
        if args.wait:
            LOG_.info(f"Waiting for {args.device} device...")
            while not serial_number:
                serial_number = server_request_device(args)
                time.sleep(5)
    return serial_number


def release_device(args: argparse.Namespace):
    server_release_device(args.serial, args)

def query_device(args: argparse.Namespace):
    grpc_device = GRPCMicroDevice(args.port, None)
    if args.enable:
        grpc_device.EnableDevice(serial_number=args.serial, status=True)
    elif args.disable:
        grpc_device.EnableDevice(serial_number=args.serial, status=False)
    else:
        print(grpc_device.RequestList())

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="Action to perform.")
    parser.add_argument(
        "--port",
        type=int,
        default=50051,
        help="RPC server port",
    )

    parser_attach = subparsers.add_parser(
        "attach", help="Request a device and attach a virtual machine."
    )
    parser_attach.set_defaults(func=attach_device)
    parser_attach.add_argument(
        "--device",
        type=str,
        required=True,
        choices=device_utils.GetAllDeviceTypes(),
        help="MicroTVM device to request.",
    )
    parser_attach.add_argument(
        "--vm-path",
        type=pathlib.Path,
        required=True,
        help="Path to Reference virtualbox.",
    )
    parser_attach.add_argument(
        "--wait", action="store_true", help="Wait if device not available."
    )
    parser_attach.add_argument(
        "--artifact-path",
        type=pathlib.Path,
        default=None,
        help="Path to store device artifact.",
    )

    parser_detach = subparsers.add_parser(
        "detach",
        help="Detach the device from virtual machine and release from device server.",
    )
    parser_detach.set_defaults(func=detach_device)
    parser_detach.add_argument(
        "--device",
        type=str,
        required=True,
        choices=device_utils.GetAllDeviceTypes(),
        help="MicroTVM device to request.",
    )
    parser_detach.add_argument(
        "--vm-path",
        type=pathlib.Path,
        required=True,
        help="Path to Reference virtualbox.",
    )
    parser_detach.add_argument(
        "--artifact-path",
        type=pathlib.Path,
        default=None,
        help="Path device artifact serial number file. Use this or --serial for serial number.",
    )
    parser_detach.add_argument(
        "--serial", type=str, default=None, help="Device serial number."
    )

    parser_request = subparsers.add_parser(
        "request", help="Request a device from device server."
    )
    parser_request.set_defaults(func=request_device)
    parser_request.add_argument(
        "--wait", action="store_true", help="Wait if device not available."
    )

    parser_release = subparsers.add_parser(
        "release", help="Release a device from device server."
    )
    parser_release.set_defaults(func=release_device)
    parser_release.add_argument(
        "--serial", type=str, default=None, help="Device serial number."
    )

    parser_query = subparsers.add_parser(
        "query", help="Query devices from server."
    )
    parser_query.set_defaults(func=query_device)
    parser_query.add_argument(
        "--enable", action="store_true", help="Enable a device on server."
    )
    parser_query.add_argument(
        "--disable", action="store_true", help="Disable a device on server."
    )
    parser_query.add_argument(
        "--serial", type=str, default=None, help="Device serial number. Used with enable/disable sub-command."
    )

    return parser.parse_args()


def main():
    args = parse_args()
    logging.basicConfig(level=logging.INFO)
    args.func(args)


if __name__ == "__main__":
    main()
