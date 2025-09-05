# FLAPPY-BIRD-python-version
A faithful clone of the popular mobile game "Flappy Bird", implemented using **PyGame**. This project demonstrates core game development concepts including physics simulation, collision detection, and state management.
<img width="214" height="414" alt="Screenshot 2025-09-05 at 11 33 09 AM" src="https://github.com/user-attachments/assets/4d1137c6-a5ad-49d7-a2eb-7adb42d9a136" />

## Features

- **Physics-Based Gameplay**: Realistic gravity and jump mechanics.
- **Collision Detection**: Pixel-perfect collision with pipes and screen boundaries.
- **Dynamic Obstacles**: Randomly generated pipe heights for endless challenge.
- **Score System**: Track your progress as you navigate through pipes.
- **Polished UI**: Animated bird sprite, victory and game over screens with interactive buttons.
- **Victory Condition**: Win the game by reaching a score of 20!

## How to Play

1.  Press the **SPACE** key to make the bird flap and gain altitude.
2.  Navigate through the gaps between the pipes.
3.  Each successfully passed pipe earns you **1 point**.
4.  Avoid hitting the pipes or the edges of the screen.
5.  Reach a score of **20** to achieve victory!

## Installation & Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/YourGitHubUsername/Flappy-Bird-Clone-Python.git
    cd Flappy-Bird-Clone-Python
    ```

2.  **Install dependencies** (Requires Python 3.x):
    ```bash
    pip install -r requirements.txt
    ```
    *Alternatively, install PyGame directly:*
    ```bash
    pip install pygame
    ```

3.  **Run the game**:
    ```bash
    python game.py
    ```

## Project Structure
    -game.py # Main game loop and logic
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── images/ # Asset directory
├── background.png
├── bird_wing_up.png
├── bird_wing_down.png
├── pipe_body.png
└── pipe_end.png

## Technical Implementation

- **Built With**: Python, Pygame
- **Core Concepts**:
  - Game State Management (Playing, Game Over, Victory)
  - Event-Driven Programming
  - Object-Oriented Principles (could be refactored to use Classes)
  - Sprite Animation and Rendering
  - Rectangle-Based Collision Detection (`pygame.Rect`)

## Future Enhancements

- Refactor code using Python Classes for Bird and Pipe objects.
- Add sound effects for flapping, scoring, and crashing.
- Implement a high-score system that persists between games.

## Developer

Qianjiao Zhao
  - GitHub: [@AmyMkJ] https://github.com/AmyMkJ 
