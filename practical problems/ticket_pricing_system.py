# Instructions
# Solve each question using Python.
# Use conditional statements, lists, type casting, and tuples as needed.
# Avoid using loops unless you want to challenge yourself.
# Comment your code to explain your logic.
# Test your code with different inputs to ensure it handles edge cases properly.
# Submit your Python script file (.ipynb) with solutions to all questions.
# Ensure your code is clean and well-commented.
# Ticket Pricing System

age = input("Enter the age of the person: ")

try:
    age = int(age)  # Ensure age is an integer
    if age < 5:
        ticket_price = 0    
    elif 5 <= age <= 12:
        ticket_price = 10
    elif 13 <= age <= 59:
        ticket_price = 20
    elif age >= 60:
        ticket_price = 15   
    else:
        ticket_price = None

    print(f"The ticket price is: ${ticket_price}")
except ValueError:
    print("Input value not valid.", ) 