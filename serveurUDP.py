#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import json
import requests
import urllib
UDP_IP = "127.0.0.1"
UDP_PORT = 8888
headers = {'content-type':'application/json','Authorization':'Basic a2VyaG91ZW50Om5heGl6aGU0'}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024)
    if (data == "0100FF") :
        url = 'http://127.0.0.1:8084/json.htm?type=command&param=switchlight&idx=2&switchcmd=Toggle'
        r = requests.get(url)
        device = r.json()
        print device