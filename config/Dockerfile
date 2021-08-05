FROM jenkins/jenkins:lts
ENV JAVA_OPTS=-Djenkins.install.runSetupWizard=false
ENV TZ=America/Los_Angeles

USER root
RUN mkdir /provision
COPY build/required-plugins.txt /provision/required-plugins.txt
RUN bash -c 'install-plugins.sh </provision/required-plugins.txt'

USER jenkins
