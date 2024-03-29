#!/usr/bin/python3
"""script that fetches the url of a website"""
import urllib.request
import sys
req = urllib.request.Request('https://alx-intranet.hbtn.io/status/')
with urllib.request.urlopen(req) as response:
    the_page = response.read()
