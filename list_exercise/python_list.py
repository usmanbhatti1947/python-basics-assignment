# Exercise 3-1: Names

# Store the names of a few of your friends in a list called names.
# Print each person’s name by accessing each element in the list, one at a time.
# List of friends' names
names = ["Ali", "Usman", "Ahmad", "Noor ul Huda", "Fatima"]
for name in names:
    print(name)

# Exercise 3-2: Greetings

# Start with the list you used in Exercise 3-1,
# but instead of just printing each person’s name,
# print a message to them. The text of each message should be the same,
# but each message should be personalized with the person’s name.
# Personalized greetings for each friend
for name in names:
    print(f"Hello {name}, how are you today?")



# Exercise 3-3: Your Own List

# Think of your favorite mode of transportation,
# such as a motorcycle or a car, and make a list that stores several examples.
# Use your list to print a series of statements about these items,
# such as “I would like to own a Honda motorcycle.”

# List of favorite modes of transportation
transportation = ["Honda motorcycle", "Toyota car", "Toyota SUV", "Bicycle", "Electric scooter"]
for mode in transportation:
    print(f"I would like to own a {mode}.")


# Exercise 3-4: Guest List

# Make a list that includes at least three people you’d like to invite to dinner.
# Then use your list to print a message to each person, inviting them to dinner.
# List of people to invite to dinner
dinner_guests = ["Ahmad", "Noor-ul-Huda", "Fatima"]
for guest in dinner_guests:
    print(f"Dear {guest}, I would like to invite you to dinner at my place.")



# Exercise 3-5: Changing Guest List
# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.

# Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.
# List of dinner guests
dinner_guests = ["Ahmad", "Noor-ul-Huda", "Fatima"]
print(f"Unfortunately, {dinner_guests[1]} cannot make it to dinner.")
dinner_guests[1] = "Awais"
for guest in dinner_guests:
    print(f"Dear {guest}, I would like to invite you to dinner at my place.")


# Exercise 3-6: More Guests
# You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

# Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.
# List of dinner guests
dinner_guests = ["Ahmad", "Noor ul Huda", "Fatima"]
print("I found a bigger table, so I can invite more guests!")
dinner_guests.insert(0, "Awais")
dinner_guests.insert(2, "Abdul Hadi")
dinner_guests.append("Faisal")
for guest in dinner_guests:
    print(f"Dear {guest}, I would like to invite you to dinner at my place.")

# Exercise 3-7: Shrinking Guest List
# You just found out that your new dinner table won’t arrive in time for the dinner, and you can only invite two people.
# Start with your program from Exercise 3-6. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# Remove guests from the list until only two names remain in your list. 
# Print a message to each of the two people still on your list, letting them know they are still invited.
# List of dinner guests

dinner_guests = ["Ahmad", "Noor-ul-Huda", "Fatima", "Awais", "Ali", "Sobia"]
print("Unfortunately, I can only invite two people to dinner.")
while len(dinner_guests) > 2:
    # pop() return last item in the list
    removed_guest = dinner_guests.pop()
    print(f"Sorry {removed_guest}, you are no longer invited to dinner.")
for guest in dinner_guests:
    print(f"Dear {guest}, you are still invited to dinner at my place.")



# Exercise 3-8: Seeing the World
# Think of at least five places in the world you’d like to visit.

# Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
# Use sorted() to print your list in alphabetical order without modifying the actual list.
# Show that your list is still in its original order by printing it.
# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# Show that your list is still in its original order by printing it again.
# Use reverse() to change the order of your list. Print the list to show that its order has changed.
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed.


# List of places to visit
places_to_visit = ["Tokyo", "Paris", "New York", "Sydney", "Cairo"]
print("Original list:", places_to_visit)
print("Sorted list (alphabetical):", sorted(places_to_visit))
print("List after sorted():", places_to_visit)
print("Sorted list (reverse alphabetical):", sorted(places_to_visit, reverse=True))
print("List after sorted() in reverse:", places_to_visit)
places_to_visit.reverse()
print("List after reverse():", places_to_visit)
places_to_visit.reverse()
print("List after reverse() again (back to original):", places_to_visit)
places_to_visit.sort()
print("List after sort() (alphabetical):", places_to_visit)
places_to_visit.sort(reverse=True)
print("List after sort() in reverse (reverse alphabetical):", places_to_visit)
# Exercise 3-9: Dinner Guests
# Working with the dinner guests list from previous exercises, print a message indicating the number of guests you are inviting.
# Print a message indicating that you are looking forward to seeing each guest.
# List of dinner guests
dinner_guests = ["Ahmad", "Noor-ul-Huda", "Fatima", "Awais", "Ali", "Sobia"]
print(f"Number of guests invited: {len(dinner_guests)}")
for guest in dinner_guests:
    print(f"Looking forward to seeing you, {guest}!")   

# Exercise 3-10: Every Function
# Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like.
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
# List of favorite fruits
favorite_fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]
print("Original list:", favorite_fruits)
print("Sorted list (alphabetical):", sorted(favorite_fruits))
print("List after sorted():", favorite_fruits)
favorite_fruits.reverse()
print("List after reverse():", favorite_fruits)
favorite_fruits.reverse()
print("List after reverse() again (back to original):", favorite_fruits)    
favorite_fruits.sort()
print("List after sort() (alphabetical):", favorite_fruits)
favorite_fruits.sort(reverse=True)
print("List after sort() in reverse (reverse alphabetical):", favorite_fruits)
print(f"Number of favorite fruits: {len(favorite_fruits)}")
# Print a message for each favorite fruit
for fruit in favorite_fruits:
    print(f"I really like {fruit}!")    
# Exercise 3-11: Intentional Error  
# If you haven’t already, create a program that causes an index error.
# Make sure you include a comment that explains what kind of error you are creating.
# Attempting to access an index that is out of range    
# This will cause an IndexError because the list has only 3 elements, and we are trying to access the 5th element (index 4).
my_list = [1, 2, 3]
try:
    print(my_list[4])   
except IndexError as e:
    print(f"An error occurred: {e}")    
# This code intentionally causes an IndexError by trying to access an index that does not exist in the list.
# The try-except block catches the error and prints a message.

# -----------------------------------------------------------------------

  
# List with different data types
mixed_list = ["Hello", 42, 3.14, True]
print("Mixed list:", mixed_list)    
for item in mixed_list:
    print(f"Item: {item}, Type: {type(item)}")


square_numbers = [x**2 for x in range(10)]
print("First 10 square numbers:", square_numbers)

# List of the first 20 even numbers
even_numbers = [x for x in range(0, 40, 2)]
# range(start, stop, step)
print("First 5 even numbers:", even_numbers[:5]) 
# index[0:5]   
print("Last 5 even numbers:", even_numbers[-5:])
# index[-5:] -5 start from the end of the list
print("Every second even number:", even_numbers[::2])
# index[::2] - every second number starting from index 0 step 2 = (2-1)

# Exercise 3-13: List Comprehension
# Create a list of the first 10 square numbers using list comprehension.
# Print the list of square numbers. 
# List comprehension to generate the first 10 square numbers
# This code uses list comprehension to create a list of the first 10 square numbers (0 to 9).
# It then prints the list of square numbers.    
# Exercise 3-14: List Slicing
# Create a list of the first 20 even numbers.
# Use slicing to print the first 5 even numbers, the last 5 even numbers, and every second even number. 
# This code creates a list of the first 20 even numbers (0 to 38).
# It then uses slicing to print the first 5 even numbers, the last 5 even numbers, and every second even number.  
# Exercise 3-15: List of Lists
# Create a list of lists, where each inner list contains the names of three different fruits.
# Print the outer list and each inner list separately.  
# List of lists containing names of fruits
fruits_list = [
    ["Apple", "Banana", "Cherry"],  
    ["Mango", "Orange", "Pineapple"],
    ["Grapes", "Strawberry", "Blueberry"]
]
print("Outer list of fruits:", fruits_list) #List of lists
for inner_list in fruits_list:
    print("Inner list of fruits:", inner_list)  
# This code creates a list of lists, where each inner list contains the names of three different fruits.
# It then prints the outer list and each inner list separately.


# Exercise 3-16: List of Dictionaries
# Create a list of dictionaries, where each dictionary contains information about a person (name, age, and city).
# Print the list and each person's information separately.  
# List of dictionaries containing information about people
people_list = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]
print("List of people:", people_list)   
for person in people_list:
    print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")  
# This code creates a list of dictionaries, where each dictionary contains information about a person (name, age, and city).
# It then prints the list and each person's information separately.


# Exercise 3-19: List of Mixed Types            
# Create a list that contains a mix of different data types (string, integer, float, boolean).
# Print the list and the type of each element in the list.
# List with mixed data types    
mixed_types_list = ["Hello", 42, 3.14, True, None]
print("Mixed types list:", mixed_types_list)
for item in mixed_types_list:
    print(f"Item: {item}, Type: {type(item)}")  
# This code creates a list that contains a mix of different data types (string, integer, float, boolean).
# It then prints the list and the type of each element in the list.


# Exercise 3-20: List of Functions
# Create a list of functions that perform basic arithmetic operations (addition, subtraction, multiplication, division).
# Call each function with example inputs and print the results.
# List of functions for basic arithmetic operations 
def add(x, y):
    return x + y    
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y if y != 0 else "Cannot divide by zero" 
# List of arithmetic functions
arithmetic_functions = [add, subtract, multiply, divide]    
# Example inputs
inputs = [(10, 5), (20, 4), (15, 3), (8, 2)]
# Call each function with example inputs and print the results
for func in arithmetic_functions:   
    for x, y in inputs:
        result = func(x, y)
        print(f"{func.__name__}({x}, {y}) = {result}")  
# This code creates a list of functions that perform basic arithmetic operations (addition, subtraction, multiplication, division).
# It then calls each function with example inputs and prints the results.


# Exercise 3-21: List of Classes
# Create a class that represents a simple geometric shape (e.g., Circle, Rectangle).
# Create a list of instances of this class and print their properties.
# Class representing a Circle   
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2  
    def circumference(self):
        return 2 * 3.14 * self.radius   
# List of Circle instances
circles = [Circle(5), Circle(10), Circle(15)]
# Print properties of each Circle instance
for circle in circles:
    print(f"Circle with radius {circle.radius}: Area = {circle.area()}, Circumference = {circle.circumference()}")  
# This code creates a class that represents a simple geometric shape (Circle).
# It then creates a list of instances of this class and prints their properties (area and circumference).


# Exercise 3-22: List of Custom Objects
# Create a custom object that represents a book (title, author, year).
# Create a list of books and print their details.
# Class representing a Book 
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
# List of Book instances
books = [
    Book("To Kill a Mockingbird", "Harper Lee", 1960),  
    Book("1984", "George Orwell", 1949),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
]
# Print details of each Book instance
for book in books:
    print(book) 
# This code creates a custom object that represents a book (title, author, year).
# It then creates a list of books and prints their details using the __str__ method.


# Exercise 3-23: List of Custom Functions
# Create a custom function that performs a specific task (e.g., calculating the factorial of a number).
# Create a list of these functions and call each function with example inputs.
# Custom function to calculate factorial    
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
# List of custom functions
custom_functions = [factorial]
# Example inputs
inputs = [0, 1, 5, 10]  
# Call each function with example inputs and print the results
for func in custom_functions:
    for n in inputs:
        result = func(n)
        print(f"{func.__name__}({n}) = {result}")   
# This code creates a custom function that performs a specific task (calculating the factorial of a number).
# It then creates a list of these functions and calls each function with example inputs, printing the results.


# Exercise 3-24: List of Custom Exceptions
# Create a custom exception class that represents an error in your application.
# Create a list of these exceptions and raise them with example messages.
# Custom exception class
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)   
# List of custom exceptions
custom_exceptions = [
    CustomError("This is a custom error message 1"),    
    CustomError("This is a custom error message 2"),
    CustomError("This is a custom error message 3")
]   
# Raise each custom exception with example messages
for exc in custom_exceptions:
    try:    
        raise exc
    except CustomError as e:
        print(f"Caught an exception: {e}")  
# This code creates a custom exception class that represents an error in your application.
# It then creates a list of these exceptions and raises them with example messages, catching and printing the exceptions.


# # Exercise 3-25: List of Custom Iterators
# # Create a custom iterator that generates a sequence of numbers (e.g., Fibonacci sequence).
# # Create a list of these iterators and iterate through them to print the generated numbers.
# # Custom iterator for Fibonacci sequence
# class FibonacciIterator:
#     def __init__(self, n):
#         self.n = n
#         self.a, self.b = 0, 1
#         self.count = 0  
#     def __iter__(self):
#         return self 
#     def __next__(self):
#         if self.count < self.n:
#             result = self.a
#             self.a, self.b = self.b, self.a + self.b
#             self.count += 1
#             return result
#         else:
#             raise StopIteration     
# # List of Fibonacci iterators
# fibonacci_iterators = [FibonacciIterator(5), FibonacciIterator(10), FibonacciIterator(15)]  
# # Iterate through each Fibonacci iterator and print the generated numbers   
# for fib_iter in fibonacci_iterators:
#     print(f"Fibonacci sequence (first {fib_iter.n} numbers):", end=" ")
#     for number in fib_iter:
#         print(number, end=" ")  
#     print()  # New line after each sequence
# # This code creates a custom iterator that generates a sequence of numbers (Fibonacci sequence).
# # It then creates a list of these iterators and iterates through them to print the generated numbers.   


# Exercise 3-28: List of Custom Modules
# Create a custom module that contains utility functions (e.g., string manipulation).
# Create a list of these modules and use their functions.
# Custom module with utility functions (string manipulation)    
def reverse_string(s):
    return s[::-1]
def to_uppercase(s):
    return s.upper()

# List of custom utility functions
utility_functions = [reverse_string, to_uppercase]
# Example strings to apply the utility functions
example_strings = ["hello", "world", "python", "programming"]       
# Use each utility function on example strings and print the results
for func in utility_functions:
    for string in example_strings:
        result = func(string)
        print(f"{func.__name__}('{string}') = '{result}'")  
# This code creates a custom module that contains utility functions (string manipulation).      
# It then creates a list of these modules and uses their functions on example strings, printing the results.


# Exercise 3-29: List of Custom Pipelines
# Create a custom pipeline that processes data (e.g., data cleaning).
# Create a list of these pipelines and apply them to example data.
# Custom pipeline for data cleaning 
def clean_data(data):
    return [item.strip().lower() for item in data if isinstance(item, str) and item.strip()]    
# List of custom pipelines
data_pipelines = [clean_data]   
# Example data to apply the pipeline
example_data = ["  Hello  ", "World", "  ", "Python", None, "  Programming  "]
# Use each custom pipeline on example data and print the results
for pipeline in data_pipelines:
    cleaned_data = pipeline(example_data)
    print(f"Cleaned data: {cleaned_data}")

# This code creates a custom pipeline that processes data (data cleaning).
# It then creates a list of these pipelines and applies them to example data, printing the cleaned results.


# Exercise 3-30: List of Custom Data Structures
# Create a custom data structure (e.g., stack, queue).
# Create a list of these data structures and perform operations on them.
# Custom stack data structure   
class Stack:
    def __init__(self):
        self.items = [] 
    def push(self, item):
        self.items.append(item) 
    def pop(self):
        if not self.is_empty():
            return self.items.pop() 
    def is_empty(self):
        return len(self.items) == 0 
    def peek(self):
        if not self.is_empty():
            return self.items[-1]   
    def size(self):
        return len(self.items)
# List of custom data structures (stacks)
stacks = [Stack(), Stack(), Stack()]
# Perform operations on each stack
for stack in stacks:
    stack.push(1)   
    stack.push(2)
    stack.push(3)
    print(f"Stack size after pushing 3 items: {stack.size()}")
    print(f"Top item (peek): {stack.peek()}")
    popped_item = stack.pop()
    print(f"Popped item: {popped_item}")
    print(f"Stack size after popping an item: {stack.size()}")  
# This code creates a custom data structure (stack) and performs operations on it.
# It then creates a list of these data structures and performs operations on each stack, printing the results.


# Exercise 3-31: List of Custom Algorithms
# Create a custom algorithm (e.g., sorting algorithm).
# Create a list of these algorithms and apply them to example data.
# Custom sorting algorithm (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
# List of custom algorithms 

custom_algorithms = [bubble_sort]   
# Example data to apply the algorithm
example_data = [64, 34, 25, 12, 22, 11, 90] 
# Use each custom algorithm on example data and print the results
for algorithm in custom_algorithms:
    sorted_data = example_data.copy()   
    algorithm(sorted_data)
    print(f"Sorted data using {algorithm.__name__}: {sorted_data}") 
# This code creates a custom algorithm (Bubble Sort) and applies it to example data.
# It then creates a list of these algorithms and applies them to the example data, printing the sorted results.


# Exercise 3-32: List of Custom Frameworks
# Create a custom framework that provides basic functionality (e.g., web framework).
# Create a list of these frameworks and use their features.
# Custom framework with basic functionality 
class CustomFramework:
    def __init__(self, name):
        self.name = name
    def run(self):  
        print(f"Running {self.name} framework...")
# List of custom frameworks
frameworks = [CustomFramework("Framework A"), CustomFramework("Framework B"), CustomFramework("Framework C")]   
# Use each custom framework and print the results
for framework in frameworks:
    framework.run()
# This code creates a custom framework that provides basic functionality (running a framework).
# It then creates a list of these frameworks and uses their features, printing the results.
