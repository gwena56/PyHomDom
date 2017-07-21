#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
global gBase, deviceLabels, groupLabels
deviceLabels = ['ID','name','group','model','status']
groupLabels = ['ID','name']
gBase = ""
device = """
CREATE TABLE IF NOT EXISTS "device" (
    `ID`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`  TEXT NOT NULL UNIQUE,
    `group` INTEGER NOT NULL,
    `model` INTEGER NOT NULL,
    `status` INTEGER
);
"""
groups = """
CREATE TABLE IF NOT EXISTS "groups" (
    `ID`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`    TEXT NOT NULL UNIQUE
);
"""
models = """
CREATE TABLE IF NOT EXISTS "models" (
    `ID`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`    TEXT NOT NULL,
    `type`    INTEGER NOT NULL,
    `sender`    INTEGER NOT NULL
);
"""

def tupleToDict(labels,tups):
    result = []
    for tup in tups:
        result.append(dict(zip(labels, tup)))
    return result

#def findDeviceByID(ID):
#    global gBase, deviceLabels, groupLabels
#    try:
#        sql = "SELECT * FROM device WHERE ID='"+str(ID)+"';"
#        result = doSqlite(sql)
#        return result['results'][0]['name']
#    except:
#        raise
# fonctions de recherche sur les devices   
def findDevice(item):
    if type(item) is int :
        try:
            sql = "SELECT * FROM device WHERE ID='"+str(item)+"';"
            result = doSqlite(sql)
            return result['results'][0]
        except:
            raise
            exit(0)
    else :
        try:
            sql = "SELECT * FROM device WHERE name='"+item+"';"
            result = doSqlite(sql)
            return result['results'][0]
        except:
            raise
            exit(0)        

#def findDeviceByName(name):
#    global gBase, deviceLabels, groupLabels
#    try:
#        sql = "SELECT * FROM device WHERE name='"+name+"';"
#        db = sqlite3.connect(gBase)
#        cursor = db.cursor()
#        cursor.execute(sql)
#        item = [cursor.fetchone()] #AZAZAZ pas bon
#        db.close()
#        return tupleToDict(deviceLabels, item)
#    except:
#        raise
    
def findDeviceID(name):
    global gBase, deviceLabels, groupLabels
    try:
        sql = "SELECT * FROM device WHERE name='"+name+"';"
        result =  doSqlite(sql)
        return result['results'][0]['ID']
    except:
        raise 
      
def findGroupID(name):
    global gBase, deviceLabels, groupLabels
    try:
        sql = "SELECT * FROM groups WHERE name='"+name+"';"
        item = doSqlite(sql)['results']
        print item
        if item[0] is not None : 
            return item[0]['ID']
        else :
            sql = "INSERT INTO groups ('name') VALUES ('"+name+"');"
            doSqlite(sql)
            sql = "SELECT * FROM groups WHERE name='"+name+"';"
            result = doSqlite(sql)['results']
            ID,name = result[0]
            return ID
    except:
        raise
# gestion du status dans la base de donnée    
def statusInit(name):
    sql ="UPDATE device SET status = 1 WHERE name = '"+ name +"';";
    doSqlite(sql)  
    return
def toggleStatus(item):
    id = findDevice(item)['ID']
    status = findDevice(item)['status']
    if (status == 1):
        status = 0
    else:
        status = 1
    sql ="UPDATE device SET status = "+str(status)+" WHERE ID = '"+ str(id) +"';";
    doSqlite(sql)  
    return status
def doSqlite(sql):
    global gBase, deviceLabels, groupLabels
    try:
        db = sqlite3.connect(gBase)
        cursor = db.cursor()
        results = []
        for row in cursor.execute(sql):
            results +=[row]
        lastRow = cursor.lastrowid
        db.commit()
        db.close()
        device = tupleToDict(deviceLabels, results)
        return {'lastRow' : lastRow, 'results' : device}
    except:
        raise
    