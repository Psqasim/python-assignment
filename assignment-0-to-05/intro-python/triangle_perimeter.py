# This program calculates the perimeter of a triangle based on user input.

# Prompting the user to enter the lengths of the three sides of the triangle
side1 = float(input("What is the length of side 1? "))  # Read input and convert to float
side2 = float(input("What is the length of side 2? "))  # Read input and convert to float
side3 = float(input("What is the length of side 3? "))  # Read input and convert to float

# Calculating the perimeter of the triangle
perimeter = side1 + side2 + side3  # Summing up all three sides

# Printing the calculated perimeter
print(f"The perimeter of the triangle is {perimeter}")
