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
# Usage: scripts/ci/2_configure_jenkins.sh [--jenkins-old-homedir <Previous Jenkins Home Directory>] [--jenkins-jobs <Path to Jenkins jobs>]
#
cd "$(dirname "$0")"
source "./ci_util.sh" || exit 2

cd "$(get_repo_root)"

if [ "$1" == "--help" ]; then
    echo "Usage: scripts/ci/2_configure_jenkins.sh [--jenkins-old-homedir <Previous Jenkins Home Directory>] [--jenkins-jobs <Path to Jenkins jobs>]"
    exit -1
fi

if [ "$1" == "--jenkins-old-homedir" ]; then
    shift 1
    old_homedir=$1
    shift 1
else
    old_homedir=${JENKINS_HOME_DIR}
fi

if [ "$1" == "--jenkins-jobs" ]; then
    shift 1
    jenkins_jobs_dir=$1
    shift 1
else
    jenkins_jobs_dir="config/jenkins-jobs"
fi

poetry run python -m python.ci.configure_jenkins \
       --base-casc-config="config/base-jenkins.yaml" \
       --nodes-file="config/nodes.json" \
       --github-personal-access-token="config/secrets/github-personal-access-token" \
       --jenkins-executor-private-key="${ARTIFACT_DIR}/executor-ssh-key" \
       --jenkins-executor-public-key="${ARTIFACT_DIR}/executor-ssh-key.pub" \
       --jenkins-homedir="${JENKINS_HOME_DIR}" \
       --jenkins-old-homedir="${old_homedir}" \
       --jenkins-jobs-config-ini="${jenkins_jobs_dir}/jenkins_jobs.ini" \
       --jenkins-jobs-files="${jenkins_jobs_dir}" \
       --jenkins-backup-dir="${BUILD_DIR}/backup"
