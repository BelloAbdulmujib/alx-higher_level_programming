#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the passed URL
"""

import urllib.parse
import urllib.request
import sys

def send_post_request(url, email):
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    
    with urllib.request.urlopen(url, data=data) as response:
          body = response.read().decode('utf-8')
        print(body)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)

