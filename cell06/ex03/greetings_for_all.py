#!/usr/bin/env python3
def greeting(text="noble stranger"):
	if isinstance(text, str):
		print(f"Hello, {text}.")
	else:
		print("Error! It was not a name.")
greeting('Alexandra')
greeting('Wil')
greeting()
greeting(42)

