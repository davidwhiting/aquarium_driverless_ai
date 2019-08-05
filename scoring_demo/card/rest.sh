#!/bin/bash

if [ $# -lt 2 ] ; then
    echo "Usage: ./rest.sh URL MODEL_ID"
    echo ""
    exit 1

else

    URL=$1
    model=$2

    echo ""
    curl \
        -d @card_data.json \
        -X POST \
        ${URL}:8080/models/${model}/score \
        -H "Content-Type: application/json"
    echo ""

    exit 0
fi
