#!/usr/bin/python

import subprocess
import time
import urllib
import usblamp

import signal
import sys

def signal_handler(signal, frame):
        print 'Code exited'
        usblamp.switchTo("off")
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
print 'Started... Press Ctrl+C to exit'

checkTime = 4

while True:
        status = urllib.urlopen('http://glynrob.com/api/rand3.php').read()
        if status == '0':
                usblamp.switchTo("green")
        elif status == '1':
                usblamp.switchTo("yellow")
        else:
                usblamp.switchTo("red")
        print status
        time.sleep(checkTime)