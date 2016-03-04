__author__ = 'Stan'

import os, sys
import serial
import time

PORT = serial.Serial("/dev/FIND_THIS_BIT", 9600, timeout=None)
initConsult()


def initConsult():
    PORT.flushInput()
    PORT.write("\xFF\xFF\xEF")
    if PORT.read(1) == "\x10":
        print("Congratulations: connected to consult successfully")
    else:
        print("unsuccessful connecting to consult")