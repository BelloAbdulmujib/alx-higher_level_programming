#!/usr/bin/python3
"""script that fetches the url of a website"""
import request
req = urllib.request.Request('https://alx-intranet.hbtn.io/status/')
with urllib.request.urlopen(req) as response:
    response = response.get(req)
