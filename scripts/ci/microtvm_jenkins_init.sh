#!/bin/bash -e

cd "$(dirname "$0")"
source "./ci_util.sh" || exit 2

container_name="microtvm-hw-ci-test"
docker_cmd=/usr/bin/docker

if [ "$(${docker_cmd} ps -q -f name=${container_name})" ]; then
    ${docker_cmd} container stop ${container_name}
    if [ "$(${docker_cmd} ps -q -f name=${container_name})" ]; then
        ${docker_cmd} container rm ${container_name}
    fi
fi

${docker_cmd} run --rm --detach --name ${container_name} -v ${JENKINS_HOME_DIR}:/var/jenkins_home -p 8080:8080 microtvm-hw-ci:latest
