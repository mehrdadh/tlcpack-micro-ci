#!groovy
// -*- mode: groovy -*-

// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.

// Jenkins pipeline
// See documents at https://jenkins.io/doc/book/pipeline/jenkinsfile/

// Device List
dev_nrf5340dk = "nrf5340dk"
dev_stm32l4r5zi_nucleo = "stm32l4r5zi_nucleo"
dev_stm32f746xx_disco = "stm32f746xx_disco"
dev_stm32f746xx_nucleo = "stm32f746xx_nucleo"

// timeout in minutes
max_time = 240

def per_exec_ws(folder) {
  return "workspace/exec_${env.EXECUTOR_NUMBER}/" + folder
}

// initialize source codes
def init_git() {
  // Add more info about job node
  sh """
     echo "INFO: NODE_NAME=${NODE_NAME} EXECUTOR_NUMBER=${EXECUTOR_NUMBER}"
     """
  checkout scm
  retry(5) {
    timeout(time: 2, unit: 'MINUTES') {
      sh 'git submodule update --init -f --recursive'
    }
  }
}

def cancel_previous_build() {
    // cancel previous build if it is not on main.
    if (env.BRANCH_NAME != "main") {
        def buildNumber = env.BUILD_NUMBER as int
        // Milestone API allows us to cancel previous build
        // with the same milestone number
        if (buildNumber > 1) milestone(buildNumber - 1)
        milestone(buildNumber)
    }
}

cancel_previous_build()

def get_time() {
  def now = new Date()
  return now.format("yyMMdd.HHmm", TimeZone.getTimeZone('PST'))
}

// attach a usb device
def step_attach_device(device) {
  sh """
    ./scripts/device_attach.sh ${device}
     """
} 

// detach a usb device
def step_release_device(device) {
  sh """
    ./scripts/device_detach.sh ${device}
     """
} 

// Zephyr Test
def step_test_zephyr(device) {
  sh """
    ./tests/scripts/task_python_test_zephyr.sh ${device}
     """
}

// Zephyr AOT Test
def step_test_zephyr_aot(device) {
  sh """
    ./tests/scripts/task_python_test_zephyr_aot.sh ${device}
     """
}

def stage_dev_attach(device) {
  stage("DevAttach: ${device}") {
    step_attach_device(device)
  }
}

def stage_test(device) {
  stage("Test: ${device}") {
    try {
      step_test_zephyr(device)
    } catch (err) {
      echo "Caught: ${err}"
    }
    try {
      step_test_zephyr_aot(device)
    } catch (err) {
      echo "Caught: ${err}"
    }
  }
}

def stage_dev_detach(device) {
  stage("DevDetach: ${device}") {
    try {
      step_release_device(device)
    } catch (err) {
      echo "Caught: ${err}"
    }
  }
}

def stage_device_run_all(device) {
  stage_dev_attach(device)
  stage_test(device)
  stage_dev_detach(device)
}

node('CPU') {
  ws(per_exec_ws("microtvm-build")) {
    stage("BUILD") {
      init_git()
      sh "./scripts/build/task_rvm_build.sh"
      sh "./scripts/build/task_init_poetry.sh"
    }

    stage_device_run_all(dev_nrf5340dk)
    stage_device_run_all(dev_stm32l4r5zi_nucleo)
    stage_device_run_all(dev_stm32f746xx_disco)
    stage_device_run_all(dev_stm32f746xx_nucleo)

    stage("Final") {
      junit "pytest-results/*.xml"
      sh "./scripts/build/task_rvm_remove.sh --delete"
    }
  }
}
