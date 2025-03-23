import random  # Import the random module

def print_random_numbers():
    """
    Generates and prints 10 random numbers between 1 and 100.
    """
    for _ in range(10):  # Loop 10 times
        print(random.randint(1, 100), end=" ")  # Generate and print a random number
    print()  # Move to the next line after printing all numbers

# Run the function
print_random_numbers()
