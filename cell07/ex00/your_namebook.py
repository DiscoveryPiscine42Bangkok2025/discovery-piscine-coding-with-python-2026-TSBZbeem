#!/usr/bin/env python3
def array_of_names(name):
	all_name = []
	for f, l in name.items():
		full_name = f"{f.capitalize()} {l.capitalize()}"
		all_name.append(full_name)
	return all_name
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
