# Question: Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program: 
# hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3
def count_letters_and_digits(input_string):
    # iterate by list comprehension
    # to count letters and digits in the input string.
    # The sum function counts the number of True values returned by the condition.  
    # The isalpha() method checks if a character is a letter,
    # and isdigit() checks if it is a digit.
    letters = sum(c.isalpha() for c in input_string)
    digits = sum(c.isdigit() for c in input_string)
    return f"LETTERS {letters} DIGITS {digits}"
print(count_letters_and_digits("hello world! 123"))
