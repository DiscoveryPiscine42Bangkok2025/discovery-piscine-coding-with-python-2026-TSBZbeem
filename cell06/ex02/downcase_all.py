#!/usr/bin/env python3
import sys
def downcase_all(text):
	return text.upper()
param = sys.argv[1:]
if not param :
	print("none")
else:
	for i in param:
		result = downcase_all(i)
		print(result)
