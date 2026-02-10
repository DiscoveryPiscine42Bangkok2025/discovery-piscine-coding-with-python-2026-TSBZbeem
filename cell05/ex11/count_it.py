#!/usr/bin/env python3
import sys
total = len(sys.argv) - 1
if total == 0:
    print("none")
else:
    print("parameters: " + str(total))
    for word in sys.argv[1:]:
        length = len(word)
        print(word + ": " + str(length))
