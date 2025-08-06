# Tic-Tac-Toe (Unbeatable AI - Minimax)

This is a command-line Tic-Tac-Toe game in Python where you play as **X** against an unbeatable **AI (O)** powered by the **Minimax Algorithm**.

[Here is the screenshot](https://drive.google.com/file/d/1pO422UpR3CwD6s87W_1wWPGzeP9n5cz1/view?usp=sharing)

## Features

 Turn-based CLI gameplay
 AI opponent using Minimax (unbeatable)
 Human player = X
 AI player = O
 Win, lose or draw detection

## Getting Started

### Requirements
Python 3.x installed on your system

Game Rules
The game board is a 3x3 grid (9 positions).
You (Player X) make the first move.
Input positions from 1 to 9 like below:
1 | 2 | 3
-----------
4 | 5 | 6
-----------
7 | 8 | 9
AI will play optimally using the Minimax algorithm.
The game ends when either player wins or it results in a draw.

About the AI (Minimax Algorithm)
The AI checks all possible outcomes of each move and always selects the one with the best guaranteed result.

+1 → AI wins
-1 → Human wins
0 → Draw

Why it’s unbeatable:
The Minimax algorithm considers every possible future move and assumes the opponent plays optimally — making it mathematically impossible to beat.
