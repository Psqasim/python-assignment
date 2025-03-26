import random

def computer_guess():
    print("🤖 Let's play the Guess the Number game!")
    print("Think of a number between 1 and 100, and I'll try to guess it.")

    low = 1
    high = 100
    attempts = 0

    while True:
        # Computer makes a guess
        guess = random.randint(low, high)
        attempts += 1

        # Ask user for feedback
        print(f"\nIs your number {guess}?")
        feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

        if feedback == 'c':
            print(f"🎉 Yay! I guessed your number {guess} in {attempts} attempts!")
            break
        elif feedback == 'h':
            high = guess - 1  # Adjust range
        elif feedback == 'l':
            low = guess + 1  # Adjust range
        else:
            print("⚠️ Invalid input. Please enter 'h', 'l', or 'c'.")

# Run the game
computer_guess()
