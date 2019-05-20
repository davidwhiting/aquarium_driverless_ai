NAME = dai-training
USER = h2oai

default: buildclean

build: 
	docker build -t ${NAME} -f Dockerfile .

buildnew: 
	docker build --no-cache --pull -t ${NAME} -f Dockerfile .

buildclean:
	docker build --no-cache -t ${NAME} -f Dockerfile .

run:
	docker run -it --rm -u ${USER}:${USER} ${NAME} /bin/bash

#fetch:
#	mkdir -p s3
#	s3cmd sync s3://h2o-tutorials/ s3/

#build: fetch
#	docker build -t opsh2oai/h2o-training -f Dockerfile .

#save:
#	docker save opsh2oai/h2o-training | pigz -c > h2o-training.gz

