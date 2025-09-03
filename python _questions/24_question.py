# Write a program that will swap numbers
def swap_numbers(num):
    number = str(num)
    number = number[::-1]
    return number
# Example input
numbers = 123
swapped_numbers = swap_numbers(numbers)
print(f"Swapped numbers: {swapped_numbers}")
