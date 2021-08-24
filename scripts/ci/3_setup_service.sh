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
# Usage: scripts/ci/3_setup_service.sh
#

cd "$(dirname "$0")"
source "./ci_util.sh" || exit 2

cd "$(get_repo_root)"

if [ "$1" == "--help" ]; then
    echo "Usage: scripts/ci/3_setup_service.sh"
    exit -1
fi

poetry run python -m microtvm_ci.ci.run_jenkins \
    --jenkins-homedir="${JENKINS_HOME_DIR}" \
    --jenkins-service-script-path="$(get_repo_root)/scripts/ci/microtvm_jenkins_init.sh"
