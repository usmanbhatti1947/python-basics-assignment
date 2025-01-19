# Problem Statement:
# Write a program that:
# ● Takes input for the temperatures of two cities in Celsius.
# ● Compares the temperatures using relational operators (>, <, ==, !=).
# Prints a message like:
# City A is hotter than City B.

# temp_in_lhr = 17
# temp_in_khi = 24

# False statement as temp_in_lhr is less than temp_in_khi
# if temp_in_lhr > temp_in_khi:
#   print("krachi is hotter than lahore")

# True statement
# if temp_in_lhr < temp_in_khi:
#   print("krachi is not hotter than lahore")

# False statement as temp. for both cities are not equal
# if temp_in_lhr == temp_in_khi:
#   print("krachi is hotter than lahore")

# temp_in_lhr = 22
# temp_in_khi = 22
# if temp_in_lhr == temp_in_khi:
#   print("Both cities have same temp. value")

# When both values are not same
# if temp_in_lhr != temp_in_khi:
#   print("Krachi is hotter than Lahore")



# Combined as in if elif and else statement

temp_in_lhr = 34
temp_in_khi = 24

if temp_in_lhr > temp_in_khi:
  print("temperature in Lahore is more than Karachi")
elif temp_in_lhr < temp_in_khi:
  print("Temperature in Lahore is less than Karachi")
elif temp_in_lhr == temp_in_khi:
  print("Temperature in Lahore is equal to Karachi")
elif temp_in_lhr != temp_in_khi:
  print("temp in Lahore is not equal to Karachi")
else:
  print("Expected error in entered value")
