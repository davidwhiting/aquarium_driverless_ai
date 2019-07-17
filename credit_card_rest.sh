#!/bin/bash

URL="3.81.206.222"
model="53a16894-a519-11e9-a8ff-0242ac110002"

curl \
	-X POST \
	-d '{"fields": ["CreditLimit", "Sex", "Education", "Marriage", "Age", "Status1", "Status2", "Status3", "Status4", "Status5", "Status6", "BillAmt1", "BillAmt2", "BillAmt3", "BillAmt4", "BillAmt5", "BillAmt6", "PayAmt1", "PayAmt2", "PayAmt3", "PayAmt4", "PayAmt5", "PayAmt6"], "rows": [["20000.0", "F", "2.0", "M", "23.0", "0.0", "0.0", "-1.0", "-2.0", "5.0", "6.0", "-5.0", "-218.0", "-807.0", "-73.0", "-600.0", "-345.0", "4.0", "65.0", "3.0", "33.0", "4.0", "12.0"]]}' \
	http://${URL}:8080/models/${model}/score \
	-H "Content-Type: application/json"
