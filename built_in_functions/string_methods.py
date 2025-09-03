full_name = input("Enter your full name: ")
print(f"Hello {full_name}! Welcome to the Python world!")

# User name in Uppercase letters
print(f"Your name in uppercase is: {full_name.upper()}")

# User name in Lowercase letters
print(f"Your name in lowercase is: {full_name.lower()}")

# user name length
print(f"Your name has {len(full_name)} characters.")

# Replace spaces with hyphens in the user's name
print(f"Your name with spaces replaced by hyphens: {full_name.replace(' ', '-')}")

# Trim any leading or trailing spaces from the user's name
print(f"Your name with leading and trailing spaces removed: {full_name.strip()}")

# Replace spaces with nothing in the user's name
print(f"Your name spaces removed: {full_name.replace(" ", "")}")

# Split the user's name into a list of words
print(f"Your name split into words: {full_name.split()}")

name_without_spaces = full_name.replace(" ", "")
print(f"Your name without spaces: {name_without_spaces[0:3]}...{name_without_spaces[-3:]}")

# Calculate the user age
age = input("Enter your birth year: ")
from datetime import datetime
current_year = datetime.now().year
age = current_year - int(age)
print(f"Your age is approximately : {age} years")
