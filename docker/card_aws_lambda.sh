#!/bin/bash
# Score Card (Default) Experiment

curl \
	-X POST \
	-d @card_test.json \
	-H "x-api-key: 0fxsVspG9Z8qp5ENdMhot7gFumf92UnlaaeIXgPB" \
	https://cvpd9o84n6.execute-api.us-east-1.amazonaws.com/test/score
