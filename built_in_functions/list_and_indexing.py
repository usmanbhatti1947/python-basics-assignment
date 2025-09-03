
# List from user input
# fruit_items = input("Enter three fruits ',' separated")
fruit_items = ("Apple,Orange,Grapes")

# convert string into list
# split function splits string into list based on the separator provided
fruit_list = fruit_items.split(",")

print(fruit_list)

# Print first item 
print(fruit_list[0])

# print last item
print(fruit_list[len(fruit_list)-1])

# append method add item to the end of the list
fruit_list.append("Banana")
print(fruit_list)

# insert method adds item at a specific index
# Insert "Mango" at index 1
fruit_list.insert(1, "Mango")
print(fruit_list)

# remove method removes the first occurrence of a specified item in list
fruit_list.remove("Orange")
print(fruit_list)

# Longest fruit string
longest_fruit = max(fruit_list, key=len)
print(f"The longest fruit name is: {longest_fruit}")

# Check if "Apple" is in the list
if "Apple" in fruit_list:
    print("Apple is in the list of fruits.")
else:
    print("Apple is not in the list of fruits.")


# Check palindrome
my_name = "Alla alla"
to_lower_name = my_name.lower().replace(" ", "")
# actual value == reversed value by reverse indexing
if to_lower_name == to_lower_name[::-1]:
    print(f"{to_lower_name} is a palindrome")
else:
    print(f"{to_lower_name} is not a palindrome")


# List of numbers
numbers = [1, 2, 3, 4, 5]
max_number = max(numbers)
min_number = min(numbers)
print(f"Max number: {max_number}, Min number: {min_number}")

# Sum of numbers
sum_of_numbers = sum(numbers)
print(f"Sum of numbers: {sum_of_numbers}")

# Average of numbers
average_of_numbers = sum_of_numbers / len(numbers)
print(f"Average of numbers: {average_of_numbers}")
product_of_numbers = 1
for number in numbers:  
    product_of_numbers *= number
print(f"Product of numbers: {product_of_numbers}")

# Scenario 3
num_items = int(input("How many items are you purchasing? "))
price_per_item = float(input("What is the price per item? "))
total_cost = num_items * price_per_item
print(f"Your total cost for {num_items} items is ${total_cost:.2f}")

if total_cost > 100:
    print(f"You are eligible for a 10% discount!")
else:
    print("You are not eligible for a discount.")

total_cost_with_discount = total_cost * 0.9 if total_cost > 100 else total_cost
print(f"Your total cost after discount is ${total_cost_with_discount:.2f}")

full_name = input("Enter your full name: ")
name_no_spaces = full_name.replace(" ", "")
name_letters = list(name_no_spaces)
print(name_letters)



full_name = input("Enter your full name: ")
name_no_spaces = full_name.replace(" ", "")
name_letters = list(name_no_spaces)

half = len(name_letters) // 2
# If odd, first half is smaller
first_half = [letter.upper() for letter in name_letters[:half]]
second_half = [letter.lower() for letter in name_letters[half:]]

result = ''.join(first_half + second_half)
print(len(result))
print(f"Transformed name: {result}")



num_students = int(input("How many students are there? "))
student_names = []
student_grades = []

for i in range(num_students):
    name = input(f"Enter the name of student #{i+1}: ")
    grade = float(input(f"Enter the grade for {name}: "))
    student_names.append(name)
    student_grades.append(grade)
# print("Student Detail:", student_names, "Grades:", student_grades)
student_data = {}
for (k,j) in zip(student_names, student_grades):
    student_data[k] = j
    # print(f"Student: {k}, Grade: {j}")
print("Student Data:", student_data)

# Calculate Average Grade of Students
average_grade = sum(student_grades) / len(student_grades)
print(f"The average grade of the students is: {average_grade:.2f}")
# Find the student with the highest grade
highest_grade = max(student_grades)
lowest_grade = min(student_grades)
print(f"The highest grade is: {highest_grade:.2f}")
print(f"The lowest grade is: {lowest_grade:.2f}")
highest_grade_index = student_grades.index(highest_grade)
top_student = student_names[highest_grade_index]
print(f"The top student is {top_student} with a grade of {highest_grade:.2f}")

# Find the student with the lowest grade
lowest_grade_index = student_grades.index(lowest_grade)
lowest_grade_student = student_names[lowest_grade_index]
print(f"The student with the lowest grade is {lowest_grade_student} with a grade of {lowest_grade:.2f}")
