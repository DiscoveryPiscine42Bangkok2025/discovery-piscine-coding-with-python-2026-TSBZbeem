#!/usr/bin/env python3
def famous_births(person):
	sorted_person = sorted(person.values(), key=lambda x: int(x['date_of_birth']))
	for i in sorted_person:
		name = i['name']
		year = i['date_of_birth']
		print(f"{name} is a great scientist born in {year}.")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)
