import random

def main():
    # Generate a random number between 0 and 99
    secret_number = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")
    
    while True:
        # Get user input
        guess = int(input("Enter a guess: "))

        # Check if the guess is too high, too low, or correct
        if guess > secret_number:
            print("Your guess is too high")
        elif guess < secret_number:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break  # Exit the loop when the correct number is guessed

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()

