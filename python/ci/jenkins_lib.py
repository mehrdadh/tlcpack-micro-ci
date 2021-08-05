import argparse
import contextlib
import logging
import pathlib
import subprocess
import threading
import time
import typing
import tempfile

from . import utils


_LOG = logging.getLogger(__name__)

JENKINS_SERVICE_NAME = "microtvm_jenkins.service"


def add_arguments(parser):
    parser.add_argument(
        "--jenkins-container",
        default="microtvm-hw-ci:latest",
        help="Container name to run",
    )
    parser.add_argument(
        "--jenkins-homedir",
        type=pathlib.Path,
        required=True,
        help="Path to a Jenkins homedir to build.",
    )
    parser.add_argument(
        "--jenkins-old-homedir",
        type=pathlib.Path,
        help="Path to a previous Jenkins homedir to transfer backups.",
    )
    parser.add_argument(
        "--jenkins-service-script-path",
        type=pathlib.Path,
        help="Path to jenkins service init script.",
    )
    parser.add_argument(
        "--jenkins-port",
        type=int,
        default=8080,
        help="Port number on local machine where the Jenkins HTTP port will be published",
    )


def container_exists(container_id: str):
    proc = subprocess.Popen(
        ["docker", "inspect", container_id],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    proc.wait()
    return proc.returncode == 0


def follow_logs(container_id: str, up_and_running: threading.Condition):
    proc = subprocess.Popen(
        ["docker", "logs", "-f", container_id],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        encoding="UTF-8",
    )
    did_set_condition = False
    for line in proc.stdout:
        _LOG.info("build.sh: %s", line[:-1])
        if not did_set_condition:
            if "Jenkins is fully up and running" in line:
                up_and_running.acquire()
                try:
                    up_and_running.notify()
                finally:
                    up_and_running.release()
                _LOG.info("----> Jenkins healthcheck passed")
                did_set_condition = True


def add_jenkins_args(parsed_args: argparse.Namespace, docker_args: list):
    docker_args.extend(
        ["-v", f"{utils.get_repo_root() / 'jenkins-builder'}:/jenkins-builder"]
    )
    docker_args.extend(
        ["-v", f"{parsed_args.jenkins_homedir.absolute()}:/var/jenkins_home"]
    )
    docker_args.extend(["-p", f"{parsed_args.jenkins_port}:8080"])


class JenkinsHealthCheckTimeoutError(Exception):
    """Raised when the health check is not passed within the given timeout."""


# Maximum number of seconds to wait for Jenkins to pass healthcheck. If it fails before this,
# assume it is busted.
JENKINS_LAUNCH_TIMEOUT_SEC = 5 * 60

def container_exist(container_name: str) -> bool:
    result = str(subprocess.check_output(["docker", "ps", "-a"])[:-1], "utf-8")
    if container_name in result:
        return True
    return False


def systemd_generate(jenkins_script_path: pathlib):
    systemd_file_description = f"""[Unit]
Description=MicroTVM Jenkins
After=network.target
StartLimitIntervalSec=0
[Service]
Type=simple
Restart=always
RestartSec=1
User=root
ExecStart=/bin/bash {str(jenkins_script_path)}
RemainAfterExit=True
[Install]
WantedBy=multi-user.target
"""
    with tempfile.NamedTemporaryFile() as tf:
        with open(tf.name, "w") as system_file:
            system_file.write(systemd_file_description)
        subprocess.check_call(
            ["sudo", "cp", tf.name, f"/etc/systemd/system/{JENKINS_SERVICE_NAME}"]
        )


def pre_launch_clean(container_name: str):
    # stop service
    subprocess.run(["sudo", "systemctl", "stop", JENKINS_SERVICE_NAME])
    # Stop previous container
    if container_exist(container_name):
        subprocess.check_call(["docker", "container", "stop", container_name])


def pre_launch_init(jenkins_script_path: pathlib):
    systemd_generate(jenkins_script_path=jenkins_script_path)
    # Reload service
    subprocess.check_call(["sudo", "systemctl", "daemon-reload"])


def launch_systemd(args: argparse.Namespace, container_name: str):
    assert(args.jenkins_service_script_path)
    pre_launch_clean(container_name)
    pre_launch_init(jenkins_script_path=args.jenkins_service_script_path)

    assert (
        subprocess.check_call(["sudo", "systemctl", "start", JENKINS_SERVICE_NAME]) == 0
    )


@contextlib.contextmanager
def launch_jenkins(
    args: argparse.Namespace,
    cmd_line_args: list,
    container_name: str,
    extra_docker_opts: typing.Optional[list] = None,
):

    pre_launch_clean(container_name)

    docker_args = ["docker", "run", "--rm", "--detach"] + (
        extra_docker_opts if extra_docker_opts is not None else []
    )
    add_jenkins_args(args, docker_args)
    docker_args.extend([args.jenkins_container] + cmd_line_args)
    container_id = str(
        subprocess.check_output(docker_args, cwd=utils.get_repo_root())[:-1], "utf-8"
    )
    print("container", container_id)
    up_and_running = threading.Condition(threading.Lock())
    try:
        threading.Thread(
            target=follow_logs, args=(container_id, up_and_running), daemon=True
        ).start()
        up_and_running.acquire()
        did_notify = up_and_running.wait(JENKINS_LAUNCH_TIMEOUT_SEC)
        if did_notify:
            yield container_id
        else:
            raise JenkinsHealthCheckTimeoutError(
                f"Jenkins did not pass healthcheck within {JENKINS_LAUNCH_TIMEOUT_SEC} seconds"
            )
    finally:
        signal = "TERM"
        if container_exists(container_id):
            subprocess.check_call(["docker", "kill", "-s", "TERM", container_id])
            time.sleep(0.5)
            if container_exists(container_id):
                proc = subprocess.run(
                    ["docker", "kill", "-s", "KILL", container_id], capture_output=True
                )
                if proc.returncode != 0 and "No such container" not in proc.stderr:
                    proc.check_returncode()
