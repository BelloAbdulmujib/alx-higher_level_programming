#!/usr/bin/python3
""" A script that fetches URL of a website
"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status/') as response:
    res = response.read()
