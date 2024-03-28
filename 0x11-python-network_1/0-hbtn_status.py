#!/usr/bin/python3
""" A script that fetches URL of a website
"""
import urllib.request
req = urllib.request.Request('https://alx-intranet.hbtn.io/status/')
with urllib.request.urlopen(req) as response:
    the_page = response.reaf()
