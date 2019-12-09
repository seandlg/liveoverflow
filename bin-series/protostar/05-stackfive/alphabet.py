#!/home/sean/anaconda3/bin/python
import sys

s = ""
for c in range(0x41, 0x5b):
	s += chr(c)*4

sys.stdout.write(s)

