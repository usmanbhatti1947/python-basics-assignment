# Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

# Hints:

# Use filter() to filter some elements in a list. Use lambda to define anonymous functions.
def filter_even_numbers():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)
filter_even_numbers()
