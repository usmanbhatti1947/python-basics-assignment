# Write a program to find the euclidean distance between two coordinates.
import math
def euclidean_distance(x1, y1, x2, y2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    # Alternatively, you can use math.sqrt for clarity
    math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}.")
euclidean_distance(3, 4, 7, 1)  # Example coordinates to check