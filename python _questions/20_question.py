# Write a program that take a user input of three angles 
# and will find out whether it can form a triangle or not.
def can_form_triangle(angle1, angle2, angle3):
    if angle1 + angle2 + angle3 == 180:
        print("The angles can form a triangle.")
    else:
        print("The angles cannot form a triangle.")
can_form_triangle(60, 70, 50)  # Example angles to check    
can_form_triangle(90, 45, 30)  # Example angles to check
can_form_triangle(90, 45, 45)  # Example angles to check
