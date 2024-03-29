#!/usr/bin/python3
"""script that fetches the url of a website
with the use of request function
"""
import requests
response = requests.get('https://alx-intranet.hbtn.io/status')


print("Body response:")
print(f"\t- type: {type(response.text)}")
print(f"\t- content: {response.text.encode('utf-8')}")
