# Write a program to print whether a given number is prime number or not
def is_prime(number):
    if number <= 1:
        return False    
    for i in range(2, number**0.5 + 1):
        if number % i == 0:
            return False    
    return True
# Example usage
num = 29
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")