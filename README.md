
# Memory Game

A simple memory game implemented in Python using Tkinter. The objective of the game is to find all matching pairs of images (or letters, in this case) hidden behind a grid of buttons.

## Features
- 4x4 grid of buttons with hidden images
- Randomly shuffled images for each game
- Simple GUI using Tkinter
- Highlights matched pairs in green
- Displays a congratulatory message when all matches are found

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/memory-game.git
   cd memory-game
   ```

2. Ensure you have Python installed. This code is compatible with Python 3.x.

3. Install Tkinter if it's not already installed. Tkinter usually comes pre-installed with Python. You can check if it's installed by running:
   ```sh
   python -m tkinter
   ```

   If you see a Tkinter window, it's installed. If not, you may need to install it. For example, on Ubuntu:
   ```sh
   sudo apt-get install python3-tk
   ```

## Usage

1. Run the main script to start the game:
   ```sh
   python main.py
   ```

2. A window will appear with a 4x4 grid of buttons. Click on the buttons to reveal the hidden images.

3. Try to find all matching pairs. When you find a match, the buttons will be highlighted in green. If you find all matches, a congratulatory message will be displayed.

## File Structure

```
memory-game/
│
├── src/
│   └── memoryGame.py   # Contains the game logic and GUI setup
│
└── main.py             # Main script to start the game
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the Tkinter documentation and community for providing valuable resources and examples.
