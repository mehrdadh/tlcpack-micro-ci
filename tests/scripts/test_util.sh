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

SCRIPTS_DIR=$(dirname "${BASH_SOURCE[0]}")

function get_repo_root() {
    cd "${SCRIPTS_DIR}" && git rev-parse --show-toplevel
}


VAGRANT_SSH_CMD="vagrant ssh -c"
REPO_ROOT=$(git rev-parse --show-toplevel)

TVM_ROOT="${REPO_ROOT}/3rdparty/tvm"
APPS_MICROTVM="${TVM_ROOT}/apps/microtvm"
RVM_ZEPHYR_DIR="${APPS_MICROTVM}/reference-vm/zephyr"
STATS_DIR="${REPO_ROOT}/pytest-results"

cd ${TVM_ROOT}
if [ ! -d ${STATS_DIR} ]
then
    mkdir ${STATS_DIR}
fi

# arg1=test_name, arg2=target
function get_test_result_filepath() {
    local test_name=$1
    local target=$2
    local result="${STATS_DIR}/${test_name}_${target}.xml"
    echo $result
}
