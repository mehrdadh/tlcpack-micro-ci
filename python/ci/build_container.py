import argparse
import logging
import shutil
import subprocess
import pathlib

from . import utils

_LOG = logging.getLogger(__name__)


def build(args: argparse.Namespace, container_tag) -> list:
    jenkins_builder = utils.get_repo_root() / "jenkins-builder"
    build_dir = jenkins_builder / "build"
    if not build_dir.exists():
        build_dir.mkdir(parents=True)
    shutil.copy2(args.required_plugins, build_dir / "required-plugins.txt")
    shutil.copy2(
        utils.get_repo_root() / "config" / "Dockerfile",
        jenkins_builder / "Dockerfile",
    )
    docker_args = ["docker", "build", "--no-cache", "-t", container_tag, "."]

    proc = subprocess.Popen(
        docker_args,
        cwd=jenkins_builder,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        encoding="UTF-8",
    )
    is_capturing_to_plugins = False
    did_finish_capturing_to_plugins = False
    installed_plugins = []
    for line in proc.stdout:
        if line[-1] == "\n":
            line = line[:-1]
        _LOG.info("docker build: %s", line)
        if (
            not is_capturing_to_plugins
            and not did_finish_capturing_to_plugins
            and line.endswith("Installed plugins:")
        ):
            _LOG.info("--> capturing")
            is_capturing_to_plugins = True
            continue
        elif (
            is_capturing_to_plugins
            and not did_finish_capturing_to_plugins
            and ":" not in line
        ):
            _LOG.info("<-- captured")
            did_finish_capturing_to_plugins = True
        elif is_capturing_to_plugins and not did_finish_capturing_to_plugins:
            installed_plugins.append(line)

    proc.wait()
    assert (
        proc.returncode == 0
    ), f"command exited with code {proc.returncode}: {' '.join(docker_args)}"

    return installed_plugins


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a Jenkins container with the plugins installed"
    )

    parser.add_argument(
        "--installed-plugins",
        required=True,
        type=pathlib.Path,
        help=(
            "Path to a file which will be filled with a list of the installed "
            "plugins and their versions. This list includes dependencies of the "
            "plugins listed in --required-plugins."
        ),
    )
    parser.add_argument(
        "--required-plugins",
        required=True,
        help=(
            "Path to a text file listing the required plugins to be installed. "
            "Should be readable by install-plugins.sh in jenkins/jenkins:lts"
        ),
    )
    parser.add_argument("--container-tag", required=True, help=("Container tag."))
    return parser.parse_args()


def main():
    args = parse_args()
    logging.basicConfig(level="INFO")

    installed_plugins = build(args, args.container_tag)
    args.installed_plugins.parent.mkdir(parents=True, exist_ok=True)
    with open(args.installed_plugins, "w") as installed_f:
        for plugin in installed_plugins:
            installed_f.write(plugin)
            installed_f.write("\n")


if __name__ == "__main__":
    main()
