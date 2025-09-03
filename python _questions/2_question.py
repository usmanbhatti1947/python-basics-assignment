
# Question: 
# 28Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be: 40320
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
# num = input("Enter a number to compute its factorial: ")
import math
number = 8
# result = math.factorial(number)
# print(f"The factorial of {number} is: {result}")

# Calculate factorial using a loop
factorial = 1
for i in range(1,number + 1):
    factorial *= i
print(f"The factorial of {number} is: {factorial}")