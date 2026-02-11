#!/usr/bin/env python3
def find_the_redheads(names):
	redhead = filter(lambda name: names[name] == "red", names)
	return list(redhead)
dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))
