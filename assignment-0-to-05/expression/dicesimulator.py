import random  # Importing the random module to generate random numbers

# This program simulates rolling two dice three times to demonstrate variable scope.

def roll_dice():
    # Generating random numbers for two dice
    die1 = random.randint(1, 6)  # First die roll (1 to 6)
    die2 = random.randint(1, 6)  # Second die roll (1 to 6)
    print(f"Die 1: {die1}, Die 2: {die2}")  # Printing results

# Rolling the dice three times
print("Rolling two dice three times:")
roll_dice()  # First roll
roll_dice()  # Second roll
roll_dice()  # Third roll