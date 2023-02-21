# CS50AI-Project1-Minesweeper

## Minesweeper game with AI agent
This project implements the classic Minesweeper game with a basic GUI, using the Pygame library. Additionally, it includes a simple AI agent to play the game automatically.

## Installation and Usage
The project requires Python 3 and the Pygame library. You can install Pygame with pip:


```pip install pygame```

To run the game, open a terminal, navigate to the project directory, and run:


```python runner.py
The game GUI will open, showing the game instructions. Follow the instructions to start playing. You can click on cells to reveal them, or right-click to flag them as mines. The game ends when you reveal all cells without hitting any mine, or when you flag all mines correctly. If you lose, the game will show the location of all mines on the board.

You can also click the "AI Move" button to let the AI agent play one move for you. The agent uses a simple strategy to choose the next cell to reveal or flag. Note that the agent does not guarantee to win the game in all cases.

To reset the game, click the "Reset" button.

Files
The project consists of the following files:

* main.py: The main script to run the game.
* minesweeper.py: The implementation of the Minesweeper game logic, including the Minesweeper and MinesweeperAI classes.
* assets/fonts/OpenSans-Regular.ttf: The font file used in the GUI.
* assets/images/flag.png: The image file used to display a flag on a flagged cell.
* assets/images/mine.png: The image file used to display a mine on a revealed mine cell.

## Limitations
The current implementation of the Minesweeper game and AI agent has the following limitations:

The game board is fixed to an 8x8 grid with 8 mines. You cannot change the size of the board or the number of mines.
The AI agent uses a simple strategy based on the number of nearby mines to choose the next cell to reveal or flag. It does not use more advanced techniques, such as probabilistic reasoning or pattern recognition.
The GUI is basic and lacks some features, such as sound effects, animations, or a menu bar.

## License
This project is released under the Havard License. Feel free to use and modify the code as you wish, but please give credit to the original author. When submitting the code, avoid plagiarism.




