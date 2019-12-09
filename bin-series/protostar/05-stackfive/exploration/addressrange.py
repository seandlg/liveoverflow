#!/usr/bin/python
base = 0xbffffdf0
r = range(0xff)

for i in range(-0xff, 0xff+1):
        value = base+i
        print("0x%X" % value)

