# Question: Write a program which accepts a sequence of comma-separated numbers from console
#  and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then,
# the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
numbers = input("Enter comma-separated numbers: ")
number_list = numbers.split(",") #split method return list of strings
# Convert list of strings to tuple
number_tuple = tuple(number_list)
print("List:", number_list)
print("Tuple:", number_tuple)