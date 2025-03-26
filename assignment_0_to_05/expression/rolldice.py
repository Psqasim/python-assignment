import random  # Importing random module to generate dice rolls

# This program simulates rolling two dice and prints the results.

# Rolling two dice
roll1 = random.randint(1, 6)  # Generating a random number between 1 and 6 for the first die
roll2 = random.randint(1, 6)  # Generating a random number between 1 and 6 for the second die

# Calculating total sum of the dice
sum_rolls = roll1 + roll2  # Adding both dice results

# Printing the results
print(f"First die: {roll1}")
print(f"Second die: {roll2}")
print(f"Total: {sum_rolls}")