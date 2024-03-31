#!/bin/bash
#This script sends a JSON POST request to a URL passed as the first argument,\
#and displays the body of the response
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

URL="$1"
FILENAME="$2"

JSON_DATA=$(cat "$FILENAME")

curl -X POST -H "Content-Type: application/json" -d "$JSON_DATA" "$URL”
