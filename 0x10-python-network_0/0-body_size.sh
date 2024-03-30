#!/bin/bash
"""this  script that takes in a URL, sends a request to that URL, /
and displays the size of the body of the response
"""

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

response=$(curl -s "$url")

response_size=$(echo -n "$response" | wc -c)

echo "Response body size: $response_size bytes”
