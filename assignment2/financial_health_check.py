# 3- Financial Health Check

from profile_setup import name
# name = input("Enter your name: ")
income = int(input("Enter monthly Income: "))
expenses = int(input("Enter monthly Expenses: "))
savings = income - expenses
percentage_saving = (savings / income) * 100

if percentage_saving >= 20:
    print(f"Great Job {name} you have a strong saving habit")
else:
    if 10 <= percentage_saving <= 20:
        print(f"Good savings {name} but could save more")
    else:
        print(f"{name} Savings are extremely low need to cut expenses")


