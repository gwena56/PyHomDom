#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3 as base
from ressources import tables

class senderRF433(object):
    def __init__(self, ad, port):
        self.rxModuleAdress = ad
        self.rxModulePort = port
    def __new__(self, ad, port):
        self.rxModuleAdress = ad
        self.rxModulePort = port
        return ad,port           
    def send(self, MESSAGE):
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.sendto(MESSAGE, (self.rxModuleAdress, self.rxModulePort))   

def newBase(chemin):
    db = base.connect(chemin)
    cursor = db.cursor()
    cursor.execute(tables.device)
    cursor.execute(tables.groups)
    cursor.execute(tables.models)
    db.commit()
    db.close()
    return chemin