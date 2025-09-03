# Question 4: Username Validator
# Write a Python program that:

# Asks the user to input a username.
# Checks if the username is valid using the following rules:
# The username must be between 5 and 15 characters long.
# The username must start with a letter (A-Z or a-z).
# Prints whether the username is valid or not.
user_name = input("Enter a username: ")
# try:
if 5 <= len(user_name) <= 15 and user_name[0].isalpha():
    is_valid = True
else:
    is_valid = False    
if is_valid:
    print("Username is valid.")
else:
    print("Username is invalid. It must be between 5 and 15 characters long and start with a letter.")
# except Exception as e:
#     print(f"An error occurred: {e}")
