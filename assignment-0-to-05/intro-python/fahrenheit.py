# Question 3 Fahrenheit to Celsius

# This program converts a temperature from Fahrenheit to Celsius.

# Prompting the user to enter temperature in Fahrenheit
degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))  # Read input and convert to float

# Converting Fahrenheit to Celsius using the formula
degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0  # Applying conversion formula

# Printing the converted temperature
print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")
