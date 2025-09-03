# Write a program that will take user input of cost price 
# and selling price and determines whether its a loss or a profit

selling_price = 22.5
purchase_price = 25.0
def check_profit_loss(purchase_price, selling_price):
    # result = selling_price - purchase_price
    # Using absolute value to ensure we get a positive result
    # This way, we can determine profit or loss without negative values
    result = abs(selling_price - purchase_price) 

    if purchase_price > selling_price:
        print("You lost: ", result) 
    else:
        print("Your profit: ", result)

check_profit_loss(purchase_price, selling_price)



# check_profit_loss(25, 22)  # Example prices to check
# check_profit_loss(30, 35)  # Example prices to check
# check_profit_loss(50, 50)  # Example prices to check  
# Uncomment the following lines to take user input
# def check_profit_loss(pp,sp):
#     result = sp - pp
#     if pp > sp:
#         print("you lost: ", result)
#     else:
#         print("your profit: ",result)

# check_profit_loss(25,22)