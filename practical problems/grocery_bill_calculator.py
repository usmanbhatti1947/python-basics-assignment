# Question 3: Grocery Bill Calculator
# Write a Python program that:

# Takes the price of 5 grocery items as input from the user.
# Calculates and prints the total bill.
# If the total bill is more than $100, it applies a 10% discount and prints the discounted total.
# Sample Input:
# Item 1 price: 20
# Item 2 price: 30
# Item 3 price: 25
# Item 4 price: 15
# Item 5 price: 10  
# Sample Output:
# Total bill: $100
# Discounted total: $90.0 

item_prices = []
for i in range(1,6):
    price = input("Enter the price of item {}: ".format(i))
    try:
        price = float(price)
        item_prices.append(price)
    except ValueError:
        print("Input value not valid. Please enter a numeric value.")
        item_prices.append(0)   

total_bill = sum(item_prices)
print("Total bill: ${}".format(total_bill))
if total_bill > 100:
    discount = total_bill * .10
    discounted_total = total_bill - discount
    print(f'total bill after discount: ${discounted_total:.2f}')
else:
    print("No discount applied.")   
