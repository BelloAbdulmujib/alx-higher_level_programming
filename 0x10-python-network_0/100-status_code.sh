#!/bin/bash
#This script sends a request to a URL passed as an argument,
#and displays only the status code of the response
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

http_response=$(curl -s -w "%{http_code}" "$1")

echo "HTTP Status Code: $http_response”
