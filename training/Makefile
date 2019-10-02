NAME = dai-training
USER = h2oai
VERSION = 1.7.0
DOCKERFILE = Dockerfile-${VERSION}
DOCKERNAME = ${NAME}:${VERSION}

default: build

# save data
push:
	s3cmd sync contents/data/ s3://whiting-aquarium-dai/contents/data/

# retrieve data
fetch:
	mkdir -p contents/data
	s3cmd sync s3://whiting-aquarium-dai/contents/data/ contents/data/

build:
	docker build -t ${DOCKERNAME} -f ${DOCKERFILE} .

buildnew:
	docker build --no-cache --pull -t ${DOCKERNAME} -f ${DOCKERFILE} .

buildclean:
	docker build --no-cache -t ${DOCKERNAME} -f ${DOCKERFILE} .

run:
	docker run -it --rm -u ${USER}:${USER} ${DOCKERNAME} /bin/bash

#save:
#	docker save opsh2oai/h2o-training | pigz -c > h2o-training.gz

