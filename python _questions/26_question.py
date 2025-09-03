# Write a program to print the first 25 odd numbers
def print_first_25_odd_numbers():
    odd_numbers = []
    for i in range(1, 50, 2):  # Start from 1, go up to 50, step by 2
        odd_numbers.append(i)
    return odd_numbers
# Example usage
first_25_odd_numbers = print_first_25_odd_numbers()
print(f"The first 25 odd numbers are: {first_25_odd_numbers}")  
