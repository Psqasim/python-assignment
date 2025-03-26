# 🎩 Hangman Game

## Overview
A classic word-guessing game where players try to guess a hidden word letter by letter before running out of lives.

## Features
- Random word selection from a predefined list
- Limited number of wrong guesses (6 lives)
- Real-time feedback on guessed letters
- Progress tracking
- User-friendly interface with emojis

## Game Mechanics
- 🔤 Guess one letter at a time
- 💀 Lose a life for each wrong guess
- 🏆 Guess the entire word to win
- ❤️ Start with 6 lives

## How to Play
1. The game randomly selects a word
2. You'll see the word as underscores representing hidden letters
3. Guess letters one at a time
4. Correct guesses reveal letters in the word
5. Incorrect guesses reduce your lives
6. Guess the entire word before losing all lives

## Requirements
- Python 3.x
- `random` module (included in standard Python library)

## Installation
No special installation required. Just clone the repository or download the script.

## Running the Game
```bash
python hangman.py
```

## Google Colab
You can also play the game directly in Google Colab:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1WyioxwpEIVewz_NKESwDmdCWtnpZ1WVH)

## Example Gameplay
```
🎩 Welcome to Hangman! Try to guess the word. 💀

Word: _ _ _ _ _
❌ Wrong guesses: None
❤️ Lives left: 6
🔤 Enter a letter: p
✅ Good guess!

Word: p _ _ _ _
❌ Wrong guesses: None
❤️ Lives left: 6
...
```

## Game Rules
- Only single letters are accepted
- No repeating previously guessed letters
- 6 incorrect guesses result in game over

## Error Handling
- Validates input (single letter)
- Prevents duplicate letter guesses
- Provides clear feedback for each guess

## Customization
- Easy to modify word list
- Simple to adjust number of lives

## Potential Improvements
- Add difficulty levels
- Expand word list
- Implement scoring system
- Add hints or categories

## Contributing
Feel free to fork the repository and submit pull requests with improvements!

## License
[MIT]

## Fun Fact
Hangman is not just a game, but a great way to improve vocabulary and spelling skills! 📚🧠