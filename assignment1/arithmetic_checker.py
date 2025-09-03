# Problem Statement:
# Write a program that:
# 1. Takes two numbers as input.
# 2. Prompts the user to input an arithmetic operator (+, -, *, /).
# Performs the operation on the numbers and prints the result.
# [Number1] [Operator] [Number2] = [Result]

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
print(f"{number1} + {number2} = {number1 + number2}")
print(f"{number1} - {number2} = {number1 - number2}")
print(f"{number1} * {number2} = {number1 * number2}")
print(f"{number1} / {number2} = {number1 / number2}")