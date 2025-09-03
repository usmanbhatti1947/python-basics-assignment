# Write a program to find the volume of the cylinder.
import math

def cylinder_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    print(f"The volume of the cylinder with radius {radius} and height {height} is {volume:.2f}.")  
    cost = volume/1000 * 40  # Assuming volume is in cm³ and converting to litres
    print(f"The cost of the milk is: {cost:.2f} rupees.")


cylinder_volume(5, 10)  # Example radius and height to check
cylinder_volume(3, 7)