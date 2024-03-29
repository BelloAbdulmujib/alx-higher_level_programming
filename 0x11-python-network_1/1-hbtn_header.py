#!/user/bin/python3
"""script that takes in a URL, sends a request to the URL and displays the value
"""
import urllib.request
import sys

def get_x_request_id(url):
    try:
        # Send an HTTP request to the provided URL
        with urllib.request.urlopen(url) as response:
            # Retrieve the value of the X-Request-Id header
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id:
                print(f"X-Request-Id: {x_request_id}")
            else:
                print("X-Request-Id header not found in the response.")
    except urllib.error.URLError as e:
        print(f"Error fetching data from {url}: {e.reason}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_x_request_id(url)
