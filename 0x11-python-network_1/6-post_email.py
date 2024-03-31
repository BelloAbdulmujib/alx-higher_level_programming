#!/usr/python3
"""script that takes in a URL and an email address, /
sends a POST request to the passed URL /
with the email as a parameter, and finally displays the body of the response
"""
import requests
import sys


def send_post_request(url, email):
    try:
        payload = {'email': email}
        response = requests.post(url, data=payload)
        response_body = response.text
        print(f"Response Body:\n{response_body}")
    except requests.RequestException as e:
        print(f"Error sending POST request: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
