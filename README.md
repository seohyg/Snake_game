# Snake Game

This project is a simple Snake game implemented in Python. The player controls the snake using directional keys to eat food and avoid colliding with the walls or the snake's own body.

## Features

- 18x18 game board where the snake moves around
- Game ends if the snake collides with a wall or its own body
- Snake grows longer each time it eats food
- Control the snake using `W`, `A`, `S`, `D` keys

## Installation

To run this project, you need to have Python and pip installed.

1. Clone this repository:

    ```bash
    git clone https://github.com/seohyg/Snake_game.git
    cd snake_game
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## How to Run

To start the game, run the following command in your terminal:

```bash
python main.py
```
The game will start, and you can control the snake using the W, A, S, D keys.

## Game Rules
- The snake starts at a random position on the board and moves in a random direction.
- The player can change the snake's direction using keyboard inputs.
- When the snake eats food, it grows longer, and new food is placed on the board.
- The game ends when the snake collides with a wall or its own body.

## Known Issues
- Input Bug: If the user presses a key, the snake may move immediately regardless of the screen refresh cycle, causing unexpected behavior. This is a known issue and can cause the snake to move faster than intended in certain situations.

## Required Libraries
- numpy: Used for array and matrix operations
- opencv-python: Used for drawing graphical elements

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Bug reports and suggestions for improvements are also welcome.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

### **README.md File Explanation**
- **Project Overview**: Provides a brief description of the project.
- **Features**: Summarizes the key features of the game.
- **Installation**: Guides the user through the installation process to run the project.
- **How to Run**: Instructions for running the game.
- **Game Rules**: Basic rules of the game and controls.
- **Required Libraries**: Lists the necessary Python libraries for the project.
- **Contributing**: Encourages contributions and provides instructions for doing so.
- **License**: Mentions the project's licensing under the MIT License.
