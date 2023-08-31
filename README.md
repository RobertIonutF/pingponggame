# Ping Pong Game

A simple ping pong game developed using Python's `pygame` library.

## Overview

The game includes:
- A moving ball that bounces off walls and paddles.
- A player-controlled paddle (left) using the `W` and `S` keys.
- An AI-controlled paddle (right) that tracks the ball's position.
- A scoring system that displays scores for both the player and the AI.

## File Structure

- `ball.py`: Defines the `Ball` class for the game's ball.
- `paddle.py`: Defines the `Paddle` class for the paddles.
- `score.py`: Defines the `Score` class for the game's scoring system.
- `game.py`: Contains the `Game` class that encompasses the main game logic, including the game loop.
- `main.py`: The entry point to run the game.

## How to Run the Game

1. Ensure you have Python and `pygame` installed.
2. Navigate to the directory containing the game files.
3. Run the command: `python main.py`.

## How to Modify

### Ball
- To adjust ball attributes like size, color, and speed, modify the values in the `Ball` class in `ball.py`.
- The ball can be made to bounce off surfaces using the `bounce(axis)` method, where `axis` can be 'x' or 'y'.

### Paddle
- Paddle attributes like size, color, and speed can be adjusted in the `Paddle` class in `paddle.py`.
- Player paddle movement is controlled with the `W` and `S` keys. This can be altered in the `run` method of the `Game` class in `game.py`.

### Score
- The scoring mechanism is in the `Score` class in `score.py`. Modify the `increment` method for custom scoring logic.

### AI Logic
- The AI paddle's movement logic is in the `ai_move` method of the `Game` class in `game.py`. Adjust this method for different AI behavior.

## Contributions

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.
