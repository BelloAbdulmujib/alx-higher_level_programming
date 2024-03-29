#!/usr/bin/python3
"""script that fetches the url of a website
with the use of request function
"""
import url.lequest
url = 'https://alx-intranet.hbtn.io/status'
response = request.get(url)

print("Body response:")
print(f"\t- type: {type(response.content)}")
print(f"\t- content: {response.content.decode('utf-8')}")
