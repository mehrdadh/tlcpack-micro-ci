import argparse
import logging

from . import jenkins_lib
from . import utils


def main():
    parser = argparse.ArgumentParser(description="Run Jenkins Service")
    jenkins_lib.add_arguments(parser)
    args = parser.parse_args()
    logging.basicConfig(level="INFO")

    jenkins_lib.launch_systemd(args, container_name=utils.JENKINS_CONTAINER_NAME)


if __name__ == "__main__":
    main()
