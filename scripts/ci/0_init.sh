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
# Usage: scripts/ci/0_init.sh [--service-name <microTVM Service Name>] [--table-file <Device Table File>]
#
cd "$(dirname "$0")"
source "./ci_util.sh" || exit 2

cd "$(get_repo_root)"

if [ "$1" == "--help" ]; then
    echo "Usage: scripts/ci/0_init.sh [--service-name <microTVM Service Name>] [--table-file <Device Table File>]"
    exit -1
fi

if [ "$1" == "--service-name" ]; then
    shift 1
    service_name=$1
    shift 1
else
    service_name="microtvm_server.service"
fi

if [ "$1" == "--table-file" ]; then
    shift 1
    table_file="--table-file $1"
    shift 1
else
    table_file=""
fi

# Setup MicroTVM device service
if systemctl --all --type service | grep -q ${service_name}; then
    sudo systemctl stop ${service_name}
fi

service_file_path="/etc/systemd/system/${service_name}"
microtvm_server_script_path="$(get_repo_root)/scripts/ci/microtvm_server_init.sh"

# Remove previous service file
sudo rm -f "${service_file_path}"

temp_file="./service.temp"
rm -f ${temp_file}
touch ${temp_file}

cat >> ${temp_file} <<EOF
[Unit]
Description=MicroTVM Device Server
After=network.target
StartLimitIntervalSec=0
[Service]
Type=simple
Restart=always
RestartSec=1
User=$USER
ExecStart=/bin/bash ${microtvm_server_script_path} ${table_file}
[Install]
WantedBy=multi-user.target
EOF

sudo cp ${temp_file} ${service_file_path}
rm ${temp_file}

sudo systemctl start ${service_name}
