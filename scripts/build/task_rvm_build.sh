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
# Usage task_rvm_build.sh [--provision <Force to provision>]
#

cd "$(dirname "$0")"
source "../util.sh" || exit 2

provision_flag=""
if [ "$1" == "--provision" ]; then
    shift 1
    provision_flag="--provision"
fi

REPO_ROOT="$(get_repo_root)"
APPS_MICROTVM=${REPO_ROOT}/3rdparty/tvm/apps/microtvm
RVM_ZEPHYR_DIR=${APPS_MICROTVM}/reference-vm/zephyr

# Provision virtualbox
cd ${RVM_ZEPHYR_DIR}
export TVM_PROJECT_DIR=${REPO_ROOT}
export TVM_RVM_NUM_CORES=4
export TVM_RVM_RAM_BYTES=4096
echo $TVM_PROJECT_DIR
vagrant up --provider=virtualbox ${provision_flag}

