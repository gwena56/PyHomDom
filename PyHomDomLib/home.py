#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
from time import sleep
import sqlite3 as base
from ressources import tables
global rxModuleAdress, rxModulePort
class newSet(object):
    def __init__(self,module =("192.168.1.3",8888)):
        self.name=""
        self.group=""
        self.model = ""
        self.base = "" 
        ad, port = module
        self.rxModuleAdress = ad
        self.rxModulePort = port
        
    def useModule(self,module):
        ad,po = module
        self.rxModuleAdress = ad
        self.rxModulePort = po 
    
    def storeUsing(self, base):
        self.base = base
        tables.gBase = base
        
    def storeDevice(self, name, group, model):
        self.name= name
        self.group= str(tables.findGroupID(group))
        self.model = model
        vl = "'"+self.name + "','" + self.group + "', '" + self.model + "'"
        try:
            query = "INSERT INTO device ('name', 'group', 'model') VALUES ("+vl+");"
            tables.doSqlite(query)
            self.send(name,'on')
            sleep(2)
            self.send(name,'on')
            tables.statusInit(name)
            return 1
        except base.IntegrityError:
            print "[.storeDevice() ]'"+name+ "' /!\ name for <devices> must be UNIQUE !!."
            return 0
        
    def changeGroupDevice(self,name,group):
        devGroup = tables.findGroupID(group)
        try:
            sql = "UPDATE device SET 'group' = "+str(devGroup)+" WHERE name ='"+name+"';"
            tables.doSqlite(sql)
            return 1
        except:
            raise
            print "[.changeGroupDevice()    ] /!\ device update error !!."
            return 0
        
    def newGroup(self, name):
        try:
            sql = "INSERT INTO groups ('name') VALUES ('"+name+"');"
            tables.doSqlite(sql)
            return 1
        except base.IntegrityError:
            print "[.newGroup()    ]'"+name+ "' /!\ name for <groups> must be UNIQUE !!."
            return 0
        
    def getDeviceId(self,name):
        try:
            sql = "SELECT * FROM device WHERE name='"+name+"';"
            result = tables.doSqlite(sql)
            return result['results'][0]['ID']
        except:
            raise 
    
    def getDeviceName(self,id):
        try:
            sql = "SELECT * FROM device WHERE ID='"+str(id)+"';"
            result = tables.doSqlite(sql)
            return result['results'][0]['name']
        except:
            raise 

    
    def sendRaw(self,MESSAGE):
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.sendto(MESSAGE, (self.rxModuleAdress, self.rxModulePort))
        
    def send(self, item, cmd):
        res = tables.findDevice(item)
        id = res['ID']
        model = res['model']
        MESSAGE="send "+str(id)+" "+ model +" "+ cmd
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.sendto(MESSAGE, (self.rxModuleAdress, self.rxModulePort))
    
    def switchOff(self, sw):
        if type(sw) is int :
            name = self.getDeviceName(sw)
        else :
            name = sw
        self.send(name,'off')
    
    def switchOn(self, sw):
        if type(sw) is int :
            name = self.getDeviceName(sw)
        else :
            name = sw
        self.send(name,'on ')
        
## Interface Réseau
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