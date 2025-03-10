# Game2048
This repository contains a simple command-line implementation of the popular 2048 puzzle game using Python. 
The project is split into two files:

main.py – The main entry point that runs the game.
game2048.py – Contains all core logic functions (board initialization, movement, merging, checking for win/lose conditions, etc.).
How It Works
The game board is a 4×4 grid, initialized with two random cells containing the number 2.
Players can move tiles by pressing W, A, S, or D to move up, left, down, or right, respectively.
When two tiles with the same value collide, they merge into a tile with the combined value.
After every move, a new random tile (with value 2) appears in an empty spot.
If you reach 2048 in any cell, you win. If there are no available moves, the game ends.
Project Requirements and Features
Exception Handling: Handles invalid inputs (e.g., invalid keys).
Two-File Structure: A main file for running the game, and a separate file containing all the functions.

Enjoy the game！
