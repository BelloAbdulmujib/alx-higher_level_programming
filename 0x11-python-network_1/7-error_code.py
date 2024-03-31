#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL /
and displays the body of the response
"""
import requests
import sys


def fetch_url_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.RequestException as e:
        print(f"Error code: {e.response.status_code}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_url_content(url)
