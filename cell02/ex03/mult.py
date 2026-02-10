print("Enter the first number")
first_number = int(input())
print("Enter the second number")
second_number = int(input())
mult = first_number * second_number
print(f"{first_number} x {second_number} = {mult}")
if mult > 0:
	print("The result is positive.")
elif mult < 0:
	print("The result is negative.")
else:
	print("The result is positive and negative.")
