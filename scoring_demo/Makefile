NAME = card_score
USER = h2o
DOCKERFILE = dockerfile-h2o-sw

default: build

build: 
	docker build -t ${NAME} -f ${DOCKERFILE} .

buildnew: 
	docker build --no-cache --pull -t ${NAME} -f ${DOCKERFILE} .

buildclean:
	docker build --no-cache -t ${NAME} -f ${DOCKERFILE} .

run:
	docker run -it -u ${USER}:${USER} ${NAME} /bin/bash

#fetch:
#	mkdir -p s3
#	s3cmd sync s3://h2o-tutorials/ s3/

#build: fetch
#	docker build -t opsh2oai/h2o-training -f Dockerfile .

#save:
#	docker save opsh2oai/h2o-training | pigz -c > h2o-training.gz

