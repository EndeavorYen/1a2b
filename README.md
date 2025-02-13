# Bulls and Cows Game (1A2B)

This project is an implementation of the classic "Bulls and Cows" game, also known as "1A2B." The goal is to guess a secret 4-digit number with unique digits. The game includes two modes: **Player Guessing** and **Algorithm Guessing**, allowing you to play against the computer or observe how an algorithm solves the puzzle.

---

## How the Game Works

1. **The Secret Number**: 
   - A 4-digit number is randomly generated with unique digits and no leading zero.
   - Example: `1234` (valid) vs `0123` (invalid).

2. **Gameplay**:
   - The player (or algorithm) guesses the number.
   - Feedback is provided for each guess in the form of "1A2B":
     - **Bulls (A)**: Correct digit in the correct position.
     - **Cows (B)**: Correct digit in the wrong position.
   - Example:
     - Secret: `1234`
     - Guess: `1325`
     - Feedback: `2A1B` (2 Bulls for `1` and `3`, 1 Cow for `2`).

3. **Winning Condition**:
   - The game ends when the guess matches the secret number (4A0B).

---

## Features

1. **Player Mode**:
   - The player guesses the secret number.
   - Input validation ensures guesses meet the requirements (4 unique digits, no leading zero).
   - Feedback is displayed after each guess, showing the number of Bulls and Cows.

2. **Algorithm Mode**:
   - An algorithm guesses the secret number using a **minimax strategy**:
     - Calculates the worst-case number of remaining candidates for each guess.
     - Chooses the guess that minimizes this worst-case number.
   - Feedback is used to eliminate invalid candidates and refine guesses.

3. **Comparison**:
   - After both modes are completed, the program compares the number of steps (guesses) taken by the player and the algorithm.

---

## How to Run the Game

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
