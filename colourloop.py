#!/usr/bin/python

import subprocess
import time
import usblamp

checkTime = 1
arr = ("white", "yellow", "red", "blue", "green")

for i in arr:
        print i
        usblamp.switchTo(i)
        time.sleep(checkTime)

print 'Code exited'
usblamp.switchTo("off")