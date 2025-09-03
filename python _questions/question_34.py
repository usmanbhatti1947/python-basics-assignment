# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
#  Then the function needs to print the last 5 elements in the list.


def generate_squares_list():
    squares_list = [i**2 for i in range(1, 21)]
    print(squares_list[-5:])  # Print the last 5 elements in the list
generate_squares_list()


