# Task: Print statements in Python
# This script demonstrates how to use print statements in Python
print("Hello World!")
print("I am learning python")
# Task 2: Print variables in Python
# This script demonstrates how to print variables in Python 
my_name = "Usman"
age = 22
favorite_animal = "Cat"
print(my_name)
print(age)
print(favorite_animal)
favorite_snacks_price = 5.99
print(f"my favorite snacks price is ${favorite_snacks_price}")
# Task 3: Print variables with formatted string
# This script demonstrates how to print variables with formatted strings in Python  
print(f"my name is {my_name} i am {age} years old and my favorite animal is {favorite_animal}")
# Task 4: Concate strings
# This script demonstrates how to concatenate strings in Python
greeting = "Hello"
name = "Usman" 
# Concatenating strings using the + operator
full_greeting = greeting + " " + name
print(full_greeting)
# Concatenating strings using f-strings
full_greeting_fstring = f"{greeting} {name}"
print(full_greeting_fstring)
# Concatenating strings using the format() method
full_greeting_format = "{} {}".format(greeting, name)
print(full_greeting_format)
# Concatenating strings using the join() method
full_greeting_join = " ".join([greeting, name])
print(full_greeting_join)
# Task 5: Print multiple variables in one line
# This script demonstrates how to print multiple variables in one line in Python
x = 10
y = 20
z = 30
# Using f-strings to print multiple variables in one line
print(f"x: {x}, y: {y}, z: {z}")
# Add variables using math operators
# This script demonstrates how to add variables using math operators in Python
sum_result = x + y + z
print(f"The sum of x, y, and z is: {sum_result}")
# Subtract variables using math operators
# This script demonstrates how to subtract variables using math operators in Python 
difference_result = z - y - x
print(f"The difference of z, y, and x is: {difference_result}") 
# Multiply variables using math operators
# This script demonstrates how to multiply variables using math operators in Python 
product_result = x * y * z
print(f"The product of x, y, and z is: {product_result}")   
# Divide variables using math operators
# This script demonstrates how to divide variables using math operators in Python   
division_result = z / y / x
print(f"The division of z, y, and x is: {division_result}") 
# Modulus operation using math operators
# This script demonstrates how to perform modulus operation using math operators in Python  
modulus_result = z % y
print(f"The modulus of z and y is: {modulus_result}")   
# Exponentiation using math operators
# This script demonstrates how to perform exponentiation using math operators in Python
exponentiation_result = x ** 2
print(f"The exponentiation of x to the power of 2 is: {exponentiation_result}")
# Floor division using math operators   
# This script demonstrates how to perform floor division using math operators in Python
floor_division_result = z // y  
print(f"The floor division of z by y is: {floor_division_result}")


