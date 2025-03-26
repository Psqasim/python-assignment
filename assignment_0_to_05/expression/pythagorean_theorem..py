import math  # Importing math module to use sqrt function

# This program calculates the hypotenuse of a right triangle using the Pythagorean theorem.

# Prompting the user to enter the lengths of the two perpendicular sides
side_ab = float(input("Enter the length of AB: "))  # Read input and convert to float
side_ac = float(input("Enter the length of AC: "))  # Read input and convert to float

# Calculating the length of the hypotenuse using Pythagorean theorem
hypotenuse_bc = math.sqrt(side_ab**2 + side_ac**2)  # Applying the formula BC^2 = AB^2 + AC^2

# Printing the result
print(f"The length of BC (the hypotenuse) is: {hypotenuse_bc}")
