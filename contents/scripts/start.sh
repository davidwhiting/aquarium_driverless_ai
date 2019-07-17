#!/bin/bash

# Note:  This run script is meant to be run at start of instance.
#
# For Ubuntu use: ubuntu
# For Amazon Linux, RedHat or CentOS change DAI_USER to use: ec2-user

# Training image addition: add "-p 8080:8080" to the ports exposed in the docker 
# for demoing REST server deployment

DAI_USER=ubuntu
RELEASE_TAG="$(cat /home/$DAI_USER/DAI_RELEASE)"

if nvidia-smi | grep -o "failed";
  then
    echo "Starting CPU only"
    docker run --init --rm --pid=host -e DRIVERLESS_AI_CONFIG_FILE="/config/config.toml" -p 9050:9050 -p 9090:9090 -p 12345:12345 -p 54321:54321 -p 8888:8888 -p 8080:8080 -u `id -u`:`id -g` -v /home/$DAI_USER/config:/config -v /home/$DAI_USER/data:/data -v /home/$DAI_USER/log:/log -v /home/$DAI_USER/tmp:/tmp -v /home/$DAI_USER/jupyter/notebooks:/jupyter/notebooks -v /home/$DAI_USER/license:/license -v /home/$DAI_USER/demo:/demo h2oai/dai-centos7-x86_64:$RELEASE_TAG &
    echo $!>/home/$DAI_USER/tmp/h2oai.pid  
  else
    echo "Setting Persistence"
    sudo nvidia-smi -pm 1
    echo "Starting GPU Enabled"
    nvidia-docker run --init --rm --pid=host -e DRIVERLESS_AI_CONFIG_FILE="/config/config.toml" -p 9050:9050 -p 9090:9090 -p 12345:12345 -p 54321:54321 -p 8888:8888 -p 8080:8080 -u `id -u`:`id -g` -v /home/$DAI_USER/config:/config -v /home/$DAI_USER/data:/data -v /home/$DAI_USER/log:/log -v /home/$DAI_USER/tmp:/tmp -v /home/$DAI_USER/jupyter/notebooks:/jupyter/notebooks -v /home/$DAI_USER/license:/license  -v /home/$DAI_USER/demo:/demo h2oai/dai-centos7-x86_64:$RELEASE_TAG &
    echo $!>/home/$DAI_USER/tmp/h2oai.pid
fi
