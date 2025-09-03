# Question 2: Meal Recommendation
# Write a Python program that:

# Asks the user what time it is in 24-hour format (e.g., 13 for 1 PM, 18 for 6 PM).
# Recommends a meal based on the time:
# 5 AM to 11 AM: Breakfast
# 12 PM to 4 PM: Lunch
# 5 PM to 9 PM: Dinner
# 10 PM to 4 AM: Late-night Snack
# Sample Input:

# Time: 14

time = input("Enter the time in 24-hour format (0-23): ")

try:

    time = int(time)  # Ensure time is an integer
    if 5 <= time < 12:
        meal = "Breakfast"      
    elif 12 <= time < 17:
        meal = "Lunch"  
    elif 17 <= time < 21:
        meal = "Dinner"
    elif (time >= 22) or (time < 5):
        meal = "Late-night Snack"
    else:
        meal = None 

    print(f"Recommended meal: {meal}")
except ValueError:
    print("Input value not valid.") 