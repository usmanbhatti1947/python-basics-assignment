# Problem Statement:
# Write a program that:
# 1. Takes two numbers as input.
# 2. Checks and displays their relationship using these conditions:
# ○ Whether the first number is greater than, less than, or equal to the second
# number.
# ○ Whether both numbers are even or odd.

# Print the results in this format:
# Number 1: [num1]
# Number 2: [num2]
# Relationship: [Greater than/Less than/Equal]
# Both numbers are [Even/Odd/Mixed].

# number_1 = int(input("Enter first number"))
# number_2 = int(input("Enter second number"))

# print("Number 1: ",number_1)
# print("Number 2: ",number_2)

# if number_1 > number_2:
#   print("number 1 is greater than number 2")
# elif number_1 < number_2:
#   print("number 1 is less than number 2")
# else:
#   print("Both numbers are equal")

# if number_1 % 2 == 0 and number_2 % 2 == 0:
#   print("Numbers are :Even ")

# elif number_1 % 2 != 0 and number_2 % 2 != 0:
#   print("Number are :Odd")

# else:
#   print("Numbers are :Mixed")


#-------------------------------------------------------

number_1 = int(input("Enter first number"))
number_2 = int(input("Enter second number"))

print("Number 1: ",number_1)
print("Number 2: ",number_2)

if number_1 > number_2:
  #declare a variable relationship
  #value assigned at true statement
  relationship = " 1 Greater 2"
elif number_1 < number_2:
  relationship = " 1 Less than 2"
else:
  relationship = "equal"

if number_1 % 2 == 0 and number_2 % 2 == 0:
  number = "Even"

elif number_1 % 2 != 0 and number_2 % 2 != 0:
  number = "Odd"

else:
  number = "Mixed"

print("Relationship: ",relationship, ", Both numbers are: ", number )