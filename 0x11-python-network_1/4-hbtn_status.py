#!/usr/bin/python3
"""script that fetches the url of a website
with the use of request function
"""
import requests
r = requests.get('https://alx-intranet.hbtn.io/status')
r.status_code

print("Body r:")
print(f"\t- type: {type(r.content)}")
print(f"\t- content: {r.content.decode('utf-8')}")
