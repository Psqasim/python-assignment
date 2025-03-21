# This program converts feet to inches.

# Constant for inches per foot
INCHES_PER_FOOT = 12  # 12 inches in one foot

# Prompting the user to enter a length in feet
feet = float(input("Enter the length in feet: "))  # Read input and convert to float

# Converting feet to inches
inches = feet * INCHES_PER_FOOT  # Multiply feet by 12 to get inches

# Printing the result with correct singular/plural form
unit = "foot" if feet == 1 else "feet"
print(f"{feet} {unit} is equal to {inches} inches.")
