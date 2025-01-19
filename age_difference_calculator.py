# Problem Statement:
# Write a program that:
# 1. Takes the ages of two people as input.

# 2. Calculates the difference in their ages using subtraction.
# Prints the result using string formatting:
# The age difference between [Person1] and [Person2] is: [Difference]
# years.


person_1 = int(input("Enter age for person 1: "))
person_2 = int(input("Enter age for person 2: "))
difference = abs(person_1 - person_2)

print(f"Age difference between {person_1} and {person_2} is {difference} years")
# The abs function in Python is used to calculate the absolute value of a number.
# The absolute value of a number is its distance from zero on the number line,
# without considering which direction from zero the number lies.
# Hence, the result is always non-negative, regardless of whether the input number is positive or negative.