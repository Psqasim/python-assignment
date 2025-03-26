# This program divides two numbers and finds the remainder.

# Prompting the user to enter two integers
num1 = int(input("Please enter an integer to be divided: "))  # Read input and convert to integer
num2 = int(input("Please enter an integer to divide by: "))  # Read input and convert to integer

# Performing division and finding the remainder
quotient = num1 // num2  # Integer division
remainder = num1 % num2  # Modulus operator to find remainder

# Printing the result
print(f"The result of this division is {quotient} with a remainder of {remainder}")