# Write a program that can multiply 2 numbers provided by the user without using the * operator
def multiply_without_operator(a, b):
    result = 0
    for _ in range(b):
        result += a
    return result
# Example input
num1 = 5
num2 = 3
result = multiply_without_operator(num1, num2)
print(f"The result of multiplying {num1} and {num2} is: {result}")  


