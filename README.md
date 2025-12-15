# Circle Catch Game

A simple and fun pygame-based game where you try to catch moving circles with your mouse cursor.

## Description

Circle Catch is an interactive game where a colored circle appears on the screen at random positions. When you hover your mouse over the circle, it jumps to a new random position, changes color, and plays a sound effect. The game keeps track of how many circles you've successfully caught!

## Features

- Random circle positioning
- Random color generation for each catch
- Sound effects (can be disabled with `-nosound` flag)
- Resizable game window
- Score counter
- Smooth 60 FPS gameplay

## Requirements

- Python 3.x
- pygame
- numpy

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd game
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the game with:
```bash
python circle_game.py
```

### Command Line Options

- `-nosound`: Disable sound effects
  ```bash
  python circle_game.py -nosound
  ```

### Controls

- **Mouse**: Move your cursor over the circle to catch it
- **Q Key**: Quit the game
- **Window Close Button**: Exit the game

## How to Play

1. Launch the game
2. Move your mouse cursor over the red circle
3. When you touch it, the circle will move to a new random position and change color
4. Try to catch it as many times as you can!
5. Your score is displayed in the top-right corner

## License

This project is open source and available under the MIT License.
