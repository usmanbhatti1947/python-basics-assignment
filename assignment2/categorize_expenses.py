# # 4 - Categorize Expenses
income = int(input("Please Enter your income? "))
essential = int(input("How much do you spend on essentials? "))
wants = int(input("How much do you spend on wants? "))
savings = int(input("How much do you save or invest? "))
# if savings entered more than the actual amount in hand
if savings > income - (essential + wants):
    print("you entered value more than your actual remaining amount")
else:
    essentials_percentage = essential / income * 100
    wants_percentage = wants / income * 100
    savings_percentage = savings / income * 100
    remaining_amount = income - (essential + wants + savings)
    print("income ", income)
    print("Essentials ", essentials_percentage, "%")
    print("Wants ", wants_percentage, "%")
    print("Saving ",savings_percentage, "%")
    # if amount remains in hand after saving added
    if remaining_amount > 0:
        print("Remaining amount after savings ", remaining_amount, "%")
