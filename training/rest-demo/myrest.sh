#!/bin/bash

curl \
	-X POST \
	-d @card_data.json \
	http://ec2-54-203-75-129.us-west-2.compute.amazonaws.com:8080/models/b9e275f6-aec6-11e9-9d83-0242ac110002/score \
	-H "Content-Type: application/json"
