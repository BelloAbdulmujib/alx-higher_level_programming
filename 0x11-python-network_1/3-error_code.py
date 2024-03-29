#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays the body
"""
import sys
import urllib.request
import urllib.error

def fetch_url_content(url):
    try:


        with urllib.request.urlopen(url) as response:

            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

if __name__ == "__main__":


    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url_to_fetch = sys.argv[1]
    fetch_url_content(url_to_fetch)
