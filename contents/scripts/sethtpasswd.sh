#!/bin/bash

DAI_USER=ubuntu
EC2_INSTANCE_ID="`wget -q -O - http://169.254.169.254/latest/meta-data/instance-id`"

if [ -e /home/$DAI_USER/config/htpasswd ]
then
  rm /home/$DAI_USER/config/htpasswd
fi

# Whiting change for training
#htpasswd -Bbc /home/${DAI_USER}/config/htpasswd h2oai "${EC2_INSTANCE_ID}"
htpasswd -Bbc /home/${DAI_USER}/config/htpasswd h2oai h2oai
htpasswd -Bb /home/${DAI_USER}/config/htpasswd training training
