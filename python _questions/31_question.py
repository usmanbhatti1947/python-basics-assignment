# Question: Write a program that accepts a sequence of whitespace separated words as input 
# and prints the words after removing all duplicate words and sorting them alphanumerically. 
# Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again Then, 
# the output should be: again and hello makes perfect practice world
def unique_sorted_words(input_string):
    words = input_string.split()
    unique_words = set(words)
    sorted_words = sorted(unique_words)
    return ' '.join(sorted_words)
print(unique_sorted_words("hello world and practice makes perfect and hello world again"))
