FROM ubuntu:18.04
LABEL maintainer="david.whiting@h2o.ai"

# Linux
RUN \
  apt-get -y update && \
  apt-get -y install \
    wget \
    libopenblas-dev \
    opencl-headers \
    clinfo \
    vim \
    zip \
    gcc

# Install OpenCL
RUN \
  apt-get -y install ocl-icd-opencl-dev && \
  mkdir -p /etc/OpenCL/vendors && \
  echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd

# Configure locale
RUN \
  apt-get -y install locales && \
  locale-gen "en_US.UTF-8" && \
  update-locale LANG=en_US.UTF-8

ENV LANG=en_US.UTF-8

# ----- USER H2O -----

# h2o user
RUN \
  useradd -ms /bin/bash h2o && \
  usermod -a -G sudo h2o && \
  echo "h2o:h2o" | chpasswd && \
  echo 'h2o ALL=NOPASSWD: ALL' >> /etc/sudoers

USER h2o
ENV HOME="/home/h2o"
WORKDIR ${HOME}

# Install Miniconda
ENV MINICONDA_FILE=Miniconda3-latest-Linux-x86_64.sh
RUN \
  wget https://repo.anaconda.com/miniconda/${MINICONDA_FILE} && \
  bash ${MINICONDA_FILE} -b -p ${HOME}/miniconda3 && \
  rm ${MINICONDA_FILE}

ENV PATH="${HOME}/miniconda3/bin/:$PATH"

# Make license file directory
RUN \
  mkdir ${HOME}/.driverlessai

######################################################################
# ADD CONTENT HERE
######################################################################

COPY --chown=h2o docker/scorer.zip ${HOME}/
COPY --chown=h2o docker/card_aws_lambda.sh ${HOME}/
COPY --chown=h2o docker/card_test.json ${HOME}/

COPY --chown=h2o /Users/dwhiting/H2O/license.sig ${HOME}/.driverlessai/

#
#
## Miniconda
#ENV MINICONDA_FILE=Miniconda3-4.5.4-Linux-x86_64.sh
#RUN \
#  wget https://repo.continuum.io/miniconda/${MINICONDA_FILE} && \
#  bash ${MINICONDA_FILE} -b 
#  /home/h2o/Miniconda3/bin/conda create -y --name pysparkling python=2.7 anaconda && \
#  /home/h2o/Miniconda3/bin/conda create -y --name h2o python=3.6 anaconda && \
#  /home/h2o/Miniconda3/envs/h2o/bin/jupyter notebook --generate-config && \
#  sed -i "s/#c.NotebookApp.token = '<generated>'/c.NotebookApp.token = 'h2o'/" .jupyter/jupyter_notebook_config.py && \
#  rm ${MINICONDA_FILE}
#

#COPY --chown=h2o conf/pyspark/00-pyspark-setup.py /home/h2o/.ipython/profile_pyspark/startup/
#COPY --chown=h2o conf/pyspark/kernel.json /home/h2o/Miniconda3/envs/h2o/share/jupyter/kernels/pyspark/
#ENV SPARKLING_WATER_HOME=/home/h2o/bin/sparkling-water



#######################################################################
