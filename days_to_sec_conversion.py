# Problem Statement:
# Write a program that:
# 1. Takes the number of days as input.
# 2. Converts the input into seconds using this formula:
# Seconds=Days×24×60×60
# Prints the result using string formatting:
# [Days] days are equal to [Seconds] seconds.


days = int(input("Enter days: "))
days_to_sec = days * 24 * 60 * 60
print(f"{days} Days are equal to {days_to_sec} seconds")