#!/usr/bin/env python
# -*- coding: utf-8 -
from PyHomDomLib import *
import time
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--rawcommand")
parser.add_argument("--ID")
args = parser.parse_args()
duino0 = install.senderRF433("192.168.1.3",8888)
kerhouent = home.newSet()
kerhouent.storeUsing("kerhouent.db")
kerhouent.useModule(duino0)
if args.rawcommand:
    kerhouent.sendRaw(args.rawcommand)
    exit()
if args.ID:
    name = kerhouent.getDeviceId(args.ID)
print name