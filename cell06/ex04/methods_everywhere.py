#!/usr/bin/env python3
import sys
def shrink(text):
	print(text[:8])
def enlarge(text):
	z = 8 - len(text)
	print(text + ('Z' * z))
params = sys.argv[1:]
if not params:
    print("none")
else:
    for p in params:
        length = len(p)
        if length > 8:
            shrink(p)
        elif length < 8:
            enlarge(p)
        else:
            print(p)
