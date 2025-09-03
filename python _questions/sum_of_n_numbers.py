# Write a program to find the sum of first n numbers, where n will be provided by the user.
# Eg if the user provides n=10 the output should be 55.
def sum_of_first_n_numbers(n):
    # Using the formula for the sum of the first n natural numbers: n(n + 1) / 2
    return n * (n + 1) // 2
# Example input
n = 10
result = sum_of_first_n_numbers(n)
print(f"The sum of the first {n} numbers is: {result}") 
