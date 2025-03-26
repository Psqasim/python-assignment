import random

def play_round():
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    print(f"Your number is: {user_number}")
    guess = input("Do you think your number is (higher/lower) than the computer's? ").strip().lower()
    
    if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
        print(f"Correct! The computer's number was {computer_number}. You get a point!\n")
        return 1
    else:
        print(f"Wrong! The computer's number was {computer_number}. No points this round.\n")
        return 0

def main():
    rounds = int(input("Enter the number of rounds you want to play: "))
    score = 0
    
    for _ in range(rounds):
        score += play_round()

    print(f"Game over! Your final score: {score}")

if __name__ == '__main__':
    main()
