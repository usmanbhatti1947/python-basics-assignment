# Write a program that will give you the sum of 3 digits
number = "123"
sum = 0 

for digit in number:
    sum += int(digit)  # Convert each character to an integer and add to sum

print(f"The sum of the digits in {number} is: {sum}")

