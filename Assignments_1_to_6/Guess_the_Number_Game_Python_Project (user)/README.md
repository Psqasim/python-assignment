# 🤖 Computer Guess the Number Game

## Overview
An interactive game where the computer tries to guess a number you're thinking of, using a binary search strategy to minimize the number of attempts.

## Features
- Computer uses intelligent guessing algorithm
- Binary search approach for efficient number discovery
- Interactive gameplay with user feedback
- Attempt tracking
- Error handling for invalid inputs

## How to Play
1. Think of a number between 1 and 100
2. When the computer guesses, respond with:
   - 'h' if the guess is too high
   - 'l' if the guess is too low
   - 'c' if the guess is correct
3. The computer will narrow down its search based on your feedback
4. The game continues until the computer guesses your number

## Requirements
- Python 3.x
- `random` module (included in standard Python library)

## Installation
No special installation required. Just clone the repository or download the script.

## Running the Game
```bash
python computer_guess.py
```

## Google Colab
You can also play the game directly in Google Colab:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1yw-EpdQ8K9D-xicmsLdZE_0tXheidse_)

## Example Gameplay
```
🤖 Let's play the Guess the Number game!
Think of a number between 1 and 100, and I'll try to guess it.

Is your number 50?
Enter 'h' if too high, 'l' if too low, or 'c' if correct: l

Is your number 75?
Enter 'h' if too high, 'l' if too low, or 'c' if correct: h

Is your number 62?
Enter 'h' if too high, 'l' if too low, or 'c' if correct: c
🎉 Yay! I guessed your number 62 in 3 attempts!
```

## Game Mechanics
The computer uses a binary search algorithm to efficiently guess the number:
- Starts with a range of 1-100
- Makes an initial random guess
- Adjusts the search range based on user feedback
- Continues narrowing down until the correct number is found

## Error Handling
- Warns user about invalid input
- Ensures input is 'h', 'l', or 'c'

## Algorithmic Approach
- Implements a simple yet effective binary search strategy
- Minimizes the number of guesses required to find the number

## Contributing
Feel free to fork the repository and submit pull requests with improvements!

## Potential Improvements
- Add difficulty levels
- Implement more advanced guessing strategies
- Add option to change number range

## License
[MIT]