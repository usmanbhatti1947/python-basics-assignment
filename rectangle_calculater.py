# Problem Statement:
# Write a program that calculates and displays the area and perimeter of a rectangle:
# 1. Take the length and width of the rectangle as inputs.
# 2. Calculate the area and perimeter using basic arithmetic operators.
# Print the result in this format:
# Length: [length]
# Width: [width]
# Area: [area]
# Perimeter: [perimeter]

length = int(input("Enter length: "))
width = float(input("Enter width: "))
print("Length: ",length)
print("Width: ",width)
print("Area: ",length*width)
print("Perimeter: ",2*(length+width))