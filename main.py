#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyHomDomLib import *
import time
### INSTALL
#base   = install.newBase("kerhouent.db")
duino0 = install.senderRF433("192.168.1.3",8888)
### HOME DEF
kerhouent = home.newSet()
### Choix Module RF
kerhouent.useModule(duino0)
### Choix base de donnée sqlite
kerhouent.storeUsing("kerhouent.db")
### 
#kerhouent.changeGroupDevice('SON_PLACARD','CUISINE')
#kerhouent.storeDevice('DD_1TONOIR','JARVIS','DIO_FIRST')
#legroupe = 'CHAMBRES'
#kerhouent.newGroup(legroupe)
#kerhouent.storeDevice('DDRONAN',legroupe,'DIO')
#kerhouent.switchOff('SON_PLACARD')
#kerhouent.storeDevice('SON_PLACARD','CUISINE','DIO_FIRST')
#print kerhouent.getDeviceId('SON_PLACARD')
print tables.toggleStatus('SON_PLACARD')