 Bible questionnaire
Overview

Bible questionnaire is a 2D pixel-style educational game built with Python and Pygame. The player answers multiple-choice questions based on key biblical events. Each correct answer reveals part of a pixel-art monument, which falls into place. By the end of each set of questions, a complete image is formed.

The game concludes with questions about Jesus’s death and resurrection.

How It Works
The game consists of 6 events, each with 4 questions:
Garden of Eden
Parting of the Red Sea
David and Goliath
Jonah and the Whale
Noah’s Ark
Jesus’s Death and Resurrection

Each correct answer:
Drops 1/4th of an image from the top of the screen
Places it into the correct position

After 4 correct answers:
The full image (monument) is displayed

If a player answers incorrectly:
A red “WRONG” message appears
The same question repeats until correct

Requirements
Python 3.x
Pygame

Install Pygame with:
pip install pygame

File Structure
my-first-local-app/
│
├── finalproject.py
├── eden.png
├── redsea.png
├── david.png
├── whale.png
├── ark.png
├── cross.png
└── .venv/
├── README.md

Controls
Press A, B, C, or D to answer questions
Close the window to exit the game

Assets
Each image is automatically loaded