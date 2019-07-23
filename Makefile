NAME = dai-training
USER = h2oai

default: buildclean

# save data
push:
	s3cmd sync contents/data/ s3://whiting-aquarium-dai/contents/data/

# retrieve data
fetch:
	mkdir -p contents/data
	s3cmd sync s3://whiting-aquarium-dai/contents/data/ contents/data/

build: 	fetch
	docker build -t ${NAME} -f Dockerfile .

buildnew: fetch
	docker build --no-cache --pull -t ${NAME} -f Dockerfile .

buildclean: fetch
	docker build --no-cache -t ${NAME} -f Dockerfile .

run:
	docker run -it --rm -u ${USER}:${USER} ${NAME} /bin/bash

#save:
#	docker save opsh2oai/h2o-training | pigz -c > h2o-training.gz

