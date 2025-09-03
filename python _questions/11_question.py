# Write a program that will tell whether the number entered by the user is odd or even.
def is_odd_or_even(number):
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")
is_odd_or_even(10)  # Example number to check
