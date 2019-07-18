FROM ubuntu:18.04
LABEL maintainer="david.whiting@h2o.ai"

SHELL ["/bin/bash", "-c"]

# Linux
RUN \
  apt-get -y update && \
  apt-get -y install \
    wget \
    curl \
    less \
    libopenblas-dev \
    opencl-headers \
    clinfo \
    sudo \
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

# ----- USER H2OAI -----

# h2oai user
RUN \
  useradd -ms /bin/bash h2oai && \
  usermod -a -G sudo h2oai && \
  echo "h2oai:h2oai" | chpasswd && \
  echo 'h2oai ALL=NOPASSWD: ALL' >> /etc/sudoers

USER h2oai
ENV HOME="/home/h2oai"
WORKDIR ${HOME}

# Install Miniconda
ENV MINICONDA_FILE=Miniconda3-latest-Linux-x86_64.sh
ENV CONDA_PATH=${HOME}/miniconda3
#ENV CONDA_PATH=/opt/miniconda3
RUN \
  wget https://repo.anaconda.com/miniconda/${MINICONDA_FILE} && \
  bash ${MINICONDA_FILE} -b -p ${CONDA_PATH} && \
  rm ${MINICONDA_FILE} && \
  ${CONDA_PATH}/bin/conda init bash

ENV PATH="${CONDA_PATH}/bin/:$PATH"

# Create conda environment for scoring
ENV CONDA="scoring"
RUN \
  conda config --env --add channels conda-forge && \
  conda create --name ${CONDA} \
      python=3.6.5 \
      filelock=3.0.4 \
      numpy=1.15.1 \
      pandas=0.24.1 \
      pycryptodome=3.6.6 \
      requests=2.20.0  \
      scikit-learn=0.19.1 \
      scipy=1.1.0 \
      setproctitle=1.1.10 \
      statsmodels=0.9.0 \
      toml=0.9.4 \
      tornado=4.4.2 \
      thrift=0.11.0

# Make license file directory
RUN \
  mkdir ${HOME}/.driverlessai

######################################################################
# ADD CONTENT HERE
######################################################################

COPY --chown=h2oai docker/scorer.zip ${HOME}/
COPY --chown=h2oai docker/card_aws_lambda.sh ${HOME}/
COPY --chown=h2oai docker/card_test.json ${HOME}/
COPY --chown=h2oai docker/license.sig ${HOME}/.driverlessai/

RUN echo "source activate scoring" >> ~/.bashrc

# Scoring-pipeline
RUN \
  unzip scorer.zip && \
  source activate scoring && \
  pip install scoring-pipeline/*.whl
