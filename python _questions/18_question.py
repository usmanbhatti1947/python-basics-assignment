# Write a program that will check whether the number is armstrong number or not.
def is_armstrong_number(number):
    digits = [int(digit) for digit in str(number)]
    num_digits = len(digits)
    sum_of_powers = sum(digit ** num_digits for digit in digits)
    return sum_of_powers == number
print(is_armstrong_number(153))  # True
print(is_armstrong_number(123))  # False
print(is_armstrong_number(370)) # True

# An Armstrong number (also called a narcissistic number) is a number
#  that is equal to the sum of its own digits each raised to the power of the number of digits.

# For example:
# 153 is an Armstrong number because:
# 1³ + 5³ + 3³ = 1 + 125 + 27 = 153