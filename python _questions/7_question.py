# Write a program that will convert celsius value to fahrenheit
def celsius_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit using the formula
    return (celsius * 9/5) + 32

# Example Celsius value
celsius_value = 25  
fahrenheit_value = celsius_to_fahrenheit(celsius_value)
print(f"{celsius_value}°C is equal to {fahrenheit_value}°F")    
