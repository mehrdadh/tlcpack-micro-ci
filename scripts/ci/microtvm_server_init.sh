#!/bin/bash -e

cd "$(dirname "$0")"
source "./ci_util.sh" || exit 2

cd "$(get_repo_root)"

${HOME}/.poetry/bin/poetry install
${HOME}/.poetry/bin/poetry run python -m microtvm_ci.device.device_server --log-level=DEBUG
