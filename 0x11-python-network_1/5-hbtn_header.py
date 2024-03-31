#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL /
and displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys


def get_x_request_id(url):
    try:
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(f"X-Request-Id value: {x_request_id}")
        else:
            print("X-Request-Id header not found in the response.")
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_x_request_id(url)
