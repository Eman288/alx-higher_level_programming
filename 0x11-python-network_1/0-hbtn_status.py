#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""


import urllib
import urllib.request

url = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(url) as respond:
    http = respond.read()
    print(http)
