# Write a program that will reverse a four digit number.
# Also it checks whether the reverse is true.
def reverse_four_digit_number(number):
    reversed_number = str(number)[::-1]
    print(type(reversed_number))
    print( reversed_number)

    if reversed_number == number:
        # is_palindrome = True
        print(f"{number} is a palindrome.")
    else:
        # is_palindrome = False
        print(f"{number} is not a palindrome.")
reverse_four_digit_number(1234)  # Example four-digit number
