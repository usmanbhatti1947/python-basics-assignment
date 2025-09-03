# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys.
# The function should just print the values only.
def generate_squares_dict():
    squares_dict = {i: i**2 for i in range(1, 21)}
    
    # to get values in a list from dictionary
    # for value in squares_dict.values():

    # to get keys in a list from dictionary
    for value in squares_dict.keys():
        print(value)
generate_squares_dict()

