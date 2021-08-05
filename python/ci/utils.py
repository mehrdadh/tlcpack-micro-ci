import argparse
import logging
import pathlib
import subprocess
import json


_LOG = logging.getLogger(__name__)


REPO_ROOT = None

JENKINS_CONTAINER_NAME = "microtvm-hw-ci-test"


def get_repo_root() -> pathlib.Path:
    global REPO_ROOT
    if REPO_ROOT is None:
        REPO_ROOT = pathlib.Path(
            subprocess.check_output(
                ["git", "rev-parse", "--show-toplevel"], encoding="utf-8"
            ).rstrip("\n")
        )
    return REPO_ROOT


def generate_ssh_key(private_key_path, public_key_path=None):
    private_key_path.parent.mkdir(parents=True, exist_ok=True)
    private_key_path.unlink(missing_ok=True)
    subprocess.check_call(
        ["ssh-keygen", "-t", "rsa", "-b", "2048", "-N", "", "-f", str(private_key_path)]
    )
    if public_key_path is not None:
        pathlib.Path(str(private_key_path) + ".pub").rename(public_key_path)


def load_node_file(args: argparse.Namespace):
    with open(args.nodes_file) as json_file:
        data = json.load(json_file)
    return data
