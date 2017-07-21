#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import urllib
#from requests.auth import HTTPBasicAuth

#type=command&param=switchlight&idx=99&switchcmd=Toggle
url = 'http://127.0.0.1:8084/json.htm?type=command&param=switchlight&idx=2&switchcmd=Toggle'
headers = {'content-type':'application/json','Authorization':'Basic a2VyaG91ZW50Om5heGl6aGU0'}
r = requests.get(url)
device = r.json()
print device