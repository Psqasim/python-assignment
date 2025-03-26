# 🎲 Guess the Number Game(Computer)

## Overview
A fun and interactive number guessing game where players try to guess a randomly generated number between 1 and 100.

## Features
- Random number generation between 1 and 100
- Unlimited attempts to guess the correct number
- Helpful hints (too high/too low)
- Attempt tracking
- Error handling for invalid inputs

## How to Play
1. The game generates a secret number between 1 and 100
2. Enter your guess when prompted
3. Receive feedback:
   - "Too low!" if your guess is smaller than the secret number
   - "Too high!" if your guess is larger than the secret number
   - "Congrats!" when you guess correctly
4. The game will tell you how many attempts it took to guess the number

## Requirements
- Python 3.x
- `random` module (included in standard Python library)

## Installation
No special installation required. Just clone the repository or download the script.

## Running the Game
```bash
python guess_the_number.py
```

## Google Colab
You can also play the game directly in Google Colab:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1FZeB4t5CgmX2ZkoRRe5-U7KQcj5IZXLz)

## Example Gameplay
```
🎯 Welcome to the Guess the Number Game!
Enter your guess (1-100): 50
Too low! Try again.
Enter your guess (1-100): 75
Too high! Try again.
Enter your guess (1-100): 62
🎉 Congrats! You guessed the number 62 in 3 attempts.
```

## Error Handling
- Entering non-numeric values will prompt a warning
- Guesses outside the 1-100 range will trigger appropriate feedback

## Contributing
Feel free to fork the repository and submit pull requests with improvements!

## License
[MIT]