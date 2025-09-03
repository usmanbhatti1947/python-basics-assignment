# Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
def find_dogs_and_chickens(total_heads, total_legs):
    # Let x be the number of chickens and y be the number of dogs
    # We have two equations:
    # 1. x + y = total_heads (total number of heads)
    # 2. 2x + 4y = total_legs (total number of legs)
    # Rearranging the first equation gives us:
    # x = total_heads - y
    # Substituting this into the second equation gives us:
    # 2(total_heads - y) + 4y = total_legs
    # Simplifying this will allow us to find y (number of dogs) 
    for dogs in range(total_heads + 1):
        chickens = total_heads - dogs
        if 2 * chickens + 4 * dogs == total_legs:
            print(f"Number of chickens: {chickens}, Number of dogs: {dogs}")    
            