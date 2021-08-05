#!/bin/bash
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
#
# Usage: scripts/device_detach.sh <DEVICE_TYPE> [--vm-path <Path to virtual machine>]
#

cd "$(dirname "$0")"
source "./util.sh" || exit 2

cd "$(get_repo_root)"

if [ "$#" -lt 1 -o "$1" == "--help" ]; then
    echo "Usage: scripts/device_detach.sh <DEVICE_TYPE> [--vm-path <Path to virtual machine>]"
    exit -1
fi

device_type=$1
shift 1

if [ "$1" == "--vm-path" ]; then
    shift 1
    vm_path=$1
    shift 1
else
    vm_path=${RVM_PATH}
fi

source $HOME/.poetry/env
poetry run python -m python.device.device_client \
    "detach" \
    --device="${device_type}" \
    --vm-path="${vm_path}" \
    --artifact-path="${ARTIFACT_PATH}"
