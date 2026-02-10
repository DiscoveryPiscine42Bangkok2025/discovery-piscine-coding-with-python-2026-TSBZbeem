original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []
for i in original_array:
	if i > 5:
		n = i+2
		new_array.append(n)
print(f"Original array: {original_array}")
print(f"New array: {set(new_array)}")
