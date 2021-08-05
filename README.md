# MicroTVM CI Repository

## About
This repository contains scripts to launch a CI using Jenkins to test TVM repository on physical microTVM targets using a [reference virtual machine (RMV)](https://github.com/apache/tvm/tree/main/apps/microtvm/reference-vm). In addition, this repositoty contains scripts for creating a microTVM hardware fleet server which manages all connected devices and provides a client script which connects to server using gRPC and processes different queries including attaching/detaching devices to/from the RVM.

## Dependencies
- We use Jenkins docker to create an easy installation
- All python dependencies are located in a poetry file.
- We use TVM as a submodule to this repository. [Jenkinsfile](./Jenkinsfile) is an example of testing [test_zephyr, test_zephyr_aot] on multiple microTVM targets. 

## Configuration Steps
To build the jenkins container with required plugins and run it as a service under systemd, follow these steps from the main directory:
- cd `this repository`
- Initialize microTVM device server as a service
  - ```./scripts/ci/0_init.sh```
- Build Jenkins container with required [plugins](./config/plugins.txt)
  - ```./scripts/ci/1_build_container.sh```
- Build Jenkins, setup its home directory and configure Jenkins jobs
  - ```./scripts/ci/2_configure_jenkins.sh```
- Setup Jenkins to run as a service under systemd
  - ```./scripts/ci/3_setup_service.sh``` 

After these steps the Jenkins will run under `localhost:8080`. You can use your browser to setup executor nodes and run a [microtvm](./config/jenkins-jobs/microtvm.yaml) job.


### References
Jenkins configuration scripts are adapted from [tlcpack-ci](https://github.com/areusch/tlcpack-ci).
