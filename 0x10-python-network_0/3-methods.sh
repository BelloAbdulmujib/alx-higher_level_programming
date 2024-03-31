#!/bin/bash
#This script takes in a URL and displays all HTTP methods the server will accept
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

http_methods=$(curl -sI "$1" | grep -i "^Allow:" | sed 's/^Allow: //i')

if [ -n "$http_methods" ]; then
    echo "Supported HTTP methods for $1:"
    echo "$http_methods"
else
    echo "No supported HTTP methods found for $1."
fi
