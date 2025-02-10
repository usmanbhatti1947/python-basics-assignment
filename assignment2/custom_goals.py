name = input("Enter your name")
# import from financial_health_check file variable
from financial_health_check import percentage_saving
saving_goals = int(input("Provide saving goals in percentage: "))
lack_of_saving = saving_goals - percentage_saving
# print("Lack of saving", lack_of_saving)
if percentage_saving >= saving_goals:
    print(f"Congratulations,{name} ! You’ve achieved your savings goal.")
else:
    print(f"Keep working on your savings, You're {lack_of_saving}% away from your goal.")
