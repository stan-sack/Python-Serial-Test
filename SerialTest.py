__author__ = 'Stan'

import os, sys
import serial
import time



def initConsult():
    PORT.flushInput()
    PORT.write("\xFF\xFF\xEF")
    time.sleep(2)
    if PORT.read(1) == "\x10":
        print("Congratulations: connected to consult successfully")
    else:
        print("unsuccessful connecting to consult")



PORT = serial.Serial("/dev/FIND_THIS_BIT", 9600, timeout=None)
initConsult()


