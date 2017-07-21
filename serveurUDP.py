#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket

UDP_IP = "192.168.1.252"
UDP_PORT = 8888
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024)
    if (data == "0100FF") :
        print "received message:", data