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
# Usage: scripts/device_release.sh <DEVICE_TYPE> <DEVICE_SERIAL>
#

cd "$(dirname "$0")"
source "./util.sh" || exit 2

cd "$(get_repo_root)"

if [ "$#" -lt 2 -o "$1" == "--help" ]; then
    echo "Usage: scripts/device_release.sh <DEVICE_TYPE> <DEVICE_SERIAL>"
    exit -1
fi

device_type=$1
shift
device_serial=$1
shift

source $HOME/.poetry/env
poetry run python -m microtvm_ci.microtvm_device.device_client \
    "release" \
    --device="${device_type}" \
    --serial="${device_serial}"
