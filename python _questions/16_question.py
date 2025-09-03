# Write a program that will determine weather 
# when the value of temperature and humidity is provided by the user.
# TEMPERATURE(C)      HUMIDITY(%)      WEATHER

#       >= 30                             >=90                Hot and Humid
#       >= 30                             < 90                 Hot
#       <30                                >= 90               Cool and Humid
#       <30                                 <90                 Cool



# also can use if elif and else statments to determine the weather condition based on the temperature and humidity values provided by the user.

def weather_condition(temperature, humidity):
    if temperature >= 30:
        if humidity >= 90:
            return "Hot and Humid"
        else:
            return "Hot"
    else:
        if humidity >= 90:
            return "Cool and Humid"
        else:
            return "Cool"
temperature = float(input("Enter temperature in Celsius: "))
humidity = float(input("Enter humidity in percentage: "))
condition = weather_condition(temperature, humidity)
print(f"The weather condition is: {condition}")