# Problem Statement:
# Write a program that calculates how much each person needs to pay when splitting a bill:
# 1. Take the total bill amount as input.
# 2. Take the number of people as input.
# 3. Calculate each person’s share by dividing the total amount by the number of people.


total_bill_amount = int(input("Enter total bill amount"))
number_of_people = int(input("Enter number of persons"))
print("Total Bill: $",total_bill_amount)
print("Number of persons: ", number_of_people)
print("Each person pays :$",total_bill_amount/number_of_people)