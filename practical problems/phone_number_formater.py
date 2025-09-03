# Question 9: Phone Number Formatter
# Write a Python program that:

# Takes a phone number as input from the user in the format 1234567890.
# Formats the number into the standard format (123) 456-7890.
# Prints the formatted phone number.
phone_number = input("Enter a phone number (10 digits): ")

    
if len(phone_number) == 10 and phone_number.isdigit():
    formatted_number = f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"
    print(f"Formatted phone number: {formatted_number}") 
else:
    print("Invalid phone number. Please enter a 10-digit number.")  
   