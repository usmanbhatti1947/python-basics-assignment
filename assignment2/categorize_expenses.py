# # 4 - Categorize Expenses
income = int(input("Please Enter your income? "))
essential = int(input("How much do you spend on essentials? "))
wants = int(input("How much do you spend on wants? "))
savings = int(input("How much do you save or invest? "))

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
    if remaining_amount > 0:
        print("Remaining amount after savings ", remaining_amount, "%")



# # check prime number
# num = None
# if num > 1:
#     for i in range(2, num):
#         if i % 2 == 0:
#             print("number is even")
#         else:

        
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

# shahid 7:15 PM
# num = int(input('Enter the num: '))
# count =0
# for i in range(1, num+1):
#     if num % i == 0:
#         count+=1
#     else:
#         continue
# if count == 2:
#     print(f'{num} is prime')



# #  Discount Calculator 💰
# Problem:
# Write a function calculate_discount(price, is_member) that:
# Members get 20% discount.
# Non-members get 10% discount.
# 📌 Example Input & Output:
# python

# calculate_discount(100, True)  # Output: 80.0
# calculate_discount(100, False)  # Output: 90.0 
# 
# 'r': Read
# Opens the file for reading (default mode). The file must exist, or it will raise an error.
# 'w': Write
# Opens the file for writing. If the file exists, it truncates the file (empties it). If the file does not exist, it creates a new one.
# 'a': Append
# Opens the file for writing at the end (appending). If the file does not exist, it creates a new one.
# 'x': Exclusive Creation
# Opens the file for writing, but fails if the file already exists. It creates a new file if it doesn’t exist.
# 'b': Binary
# Opens the file in binary mode. It is used in combination with other modes like 'rb' or 'wb'.
# 't': Text
# Opens the file in text mode (default). You usually don't need to specify this as it is the default mode. Can be used in combination with other modes like 'rt' or 'wt'.
# 'r+': Read and Write
# Opens the file for both reading and writing. The file must exist.
# 'w+': Write and Read
# Opens the file for both writing and reading. If the file exists, it truncates it. If the file does not exist, it creates a new one.
# 'a+': Append and Read
# Opens the file for both appending and reading. Creates a new file if it doesn't exist.
# 'rb': Read Binary
# Opens the file for reading in binary mode.
# 'wb': Write Binary
# Opens the file for writing in binary mode.
# 'ab': Append Binary
# Opens the file for appending in binary mode.
# 'r+b' or 'rb+': Read and Write Binary
# Opens the file for both reading and writing in binary mode.
# 'w+b' or 'wb+': Write and Read Binary
# Opens the file for both writing and reading in binary mode. It truncates the file if it exists, otherwise creates a new file.
# 'a+b' or 'ab+': Append and Read Binary
# Opens the file for both appending and reading in   


# file = open("hello", "w")
# print(file.write("Hello guys"))