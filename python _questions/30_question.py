def capitalized_words(input_string):
    words = input_string.split(',')
    # A list comprehension is a concise way to create a new list
    #  by applying an expression to each item in an iterable (like a list).
    # In your example:
    capitalized = [word.capitalize() for word in words]
    return ','.join(capitalized)
print(capitalized_words("hello,world,python,programming"))