# Given a string s representing time in 24-hour format "HH:MM", compute the smallest angle in degrees between the hour and minute hands of an analog clock.
def clock_angle(s):
    # Split the input string into hours and minutes
    hours, minutes = map(int, s.split(':'))
    # Normalize hours to 12-hour format
    hours = hours % 12

    # Calculate the angle of the hour hand
    # Each hour, the hour hand moves 30 degrees (360° / 12 hours).
    # It also moves 0.5 degrees for each minute 
    hour_angle = (hours * 30) + (minutes * 0.5)
    # The minute hand moves 360 degrees in 60 minutes.
    # So, each minute, it moves 6 degrees (360° / 60).
    # Calculate the angle of the minute hand
    minute_angle = minutes * 6
    # Calculate the difference between the two angles
    angle = abs(hour_angle - minute_angle)
    # Ensure the angle is the smallest angle
    angle = min(angle, 360 - angle)
    print(f"The smallest angle between the hour and minute hands at {s} is {angle:.2f} degrees.")
clock_angle("06:00")  # Example time to check