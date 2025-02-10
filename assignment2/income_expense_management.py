# 2- Expenses Management

# from income_expense_management import expenses 
income = int(input("Enter monthly Income: "))
expenses = int(input("Enter monthly Expenses: "))
savings = income - expenses
percentage_saving = (savings / income) * 100

print("Your monthly savings are:", savings)
print("Total percentage of savings is: ", percentage_saving, "%" )


