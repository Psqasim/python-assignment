# This program calculates energy using Einstein's mass-energy equivalence formula.

# Defining the speed of light constant (C)
C = 299792458  # Speed of light in meters per second

while True:
    # Prompting the user to enter mass in kilograms
    mass = float(input("Enter kilos of mass: "))  # Read input and convert to float
    
    # Calculating energy using E = m * C^2
    energy = mass * C**2  # Applying Einstein's formula
    
    # Printing the results
    print("\ne = m * C^2...")
    print(f"m = {mass} kg")
    print(f"C = {C} m/s")
    print(f"{energy} joules of energy!\n")