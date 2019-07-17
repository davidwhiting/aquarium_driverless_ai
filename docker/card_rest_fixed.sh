#!/bin/bash

URL="3.81.206.222"
model="53a16894-a519-11e9-a8ff-0242ac110002"

echo ""
curl \
  -d @card_data.json \
  -X POST \
  http://${URL}:8080/models/${model}/score \
  -H "Content-Type: application/json"
echo ""
echo ""
