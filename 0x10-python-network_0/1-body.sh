#!/bin/bash
#This script that takes in a URL, sends a GET request to the URL,
#and displays the body of the response

curl -s -o temp.txt -w "%{http_code}" "$1" && [ $(tail -n1 temp.txt) -eq 200 ] && sed '$d' temp.txt
rm -f temp.txt
