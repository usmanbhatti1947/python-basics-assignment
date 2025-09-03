# Write a program that will take three digits from the user 
# and add the square of each digit.
# def sum_of_squares_of_digits(number):
#     # if not (100 <= number <= 999):
#         # raise ValueError("Number must be a three-digit integer.")
#     digits = [int(digit) for digit in str(number)]
#     sum_squares = sum(digit ** 2 for digit in digits)
#     print(f"The sum of the squares of the digits of {number} is {sum_squares}.")    
# number = int(input("Enter a three-digit integer: "))
# try:
#     sum_of_squares_of_digits(number)
# except ValueError as e:
#     print("provide integer number",e)

numbers = input("Enter a three-digit integer: ")
# digits = int(numbers[0]), int(numbers[1]), int(numbers[2])
digits = [int(digit) for digit in numbers]
sum_of_squares_of_digits = sum(digit ** 2 for digit in digits)
print(f"The sum of the squares of the digits of {numbers} is {sum_of_squares_of_digits}.")