import random

def get_winner(user, computer):
    if user == computer:
        return "It's a tie! 🤝"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "🎉 You win!"
    else:
        return "💻 Computer wins!"

def play_game():
    choices = ["rock", "paper", "scissors"]
    print("\nWelcome to Rock, Paper, Scissors! ✊📄✂️")

    while True:
        user_choice = input("\nEnter rock, paper, or scissors (or 'q' to quit): ").lower()
        
        if user_choice == 'q':
            print("👋 Thanks for playing! See you next time!")
            break
        elif user_choice not in choices:
            print("⚠️ Invalid choice! Please enter rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"\n💻 Computer chose: {computer_choice}")
        print(f"🧑 You chose: {user_choice}")

        # Determine winner
        print(get_winner(user_choice, computer_choice))

# Run the game
play_game()
