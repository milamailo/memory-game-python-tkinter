from src.memoryGame import initialize_game, create_widgets
import tkinter as tk

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Memory Game")

    # Initialize the game with the root window
    initialize_game(root)
    # Create the game widgets (buttons)
    create_widgets()

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
