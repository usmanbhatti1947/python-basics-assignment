# Write  a program that will tell whether the given number is divisible by 3 & 6
def is_divisible_by_3_and_6(number):
    if number % 3 == 0 and number % 6 == 0:
        print(f"{number} is divisible by both 3 and 6.")
    else:
        print(f"{number} is not divisible by both 3 and 6.")    

is_divisible_by_3_and_6(18)
is_divisible_by_3_and_6(10)