#!/bin/bash
#This script takes in a URL as an argument, sends a GET request to the URL,
#and displays the body of the response
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL="$1"
HEADER="X-School-User-Id: 98"

response=$(curl -s -H "$HEADER" "$URL")

echo "$response”
