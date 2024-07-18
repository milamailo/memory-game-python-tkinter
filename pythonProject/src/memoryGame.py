import tkinter as tk
from tkinter import messagebox
import random


def initialize_game(r):
    """
    Initialize the game state, including the root window, buttons, images, and choices.
    """
    global root, buttons, images, first_choice, second_choice, matches_found

    # Set the root window
    root = r

    # Initialize an empty list for the buttons
    buttons = []

    # Define the images and shuffle them
    images = ["A", "B", "C", "D", "E", "F", "G", "H"] * 2
    random.shuffle(images)

    # Reset the choices and matches found
    first_choice = None
    second_choice = None
    matches_found = 0


def create_widgets():
    """
    Create the GUI widgets, particularly the grid of buttons.
    """
    frame = tk.Frame(root)
    frame.pack()

    # Create a 4x4 grid of buttons
    for i in range(4):
        row = []
        for j in range(4):
            # Create a button and add a lambda function to handle the button click
            # The lambda function captures the current values of i and j and passes them to reveal_image
            button = tk.Button(frame, text="", width=10, height=5, command=lambda i=i, j=j: reveal_image(i, j))
            button.grid(row=i, column=j)  # Place the button in the grid
            row.append(button)  # Add the button to the current row
        buttons.append(row)  # Add the row of buttons to the list of all buttons


def reveal_image(i, j):
    """
    Reveal the image at the specified button location.
    """
    global first_choice, second_choice

    # If two choices are already made, do nothing
    if first_choice and second_choice:
        return

    # Reveal the image and disable the button
    # The index of the image is calculated as i * 4 + j to map the 2D button grid to the 1D images list
    # This converts the 2D grid coordinates (i, j) into a single index for the images list
    buttons[i][j].config(text=images[i * 4 + j], state="disabled")

    # Set the first or second choice
    if not first_choice:
        first_choice = (i, j)
    elif not second_choice:
        second_choice = (i, j)
        # Check for a match after a short delay
        root.after(500, check_match)


def check_match():
    """
    Check if the two selected images match.
    """
    global first_choice, second_choice, matches_found

    # Get the indices of the first and second choices
    i1, j1 = first_choice
    i2, j2 = second_choice

    # If the images match, keep them revealed and update the match count
    if images[i1 * 4 + j1] == images[i2 * 4 + j2]:
        matches_found += 1
        buttons[i1][j1].config(bg="light green")  # Highlight the matched buttons
        buttons[i2][j2].config(bg="light green")
        # If all matches are found, show a congratulatory message
        if matches_found == 8:
            messagebox.showinfo("Memory Game", "Congratulations! You found all matches!")
    else:
        # If the images don't match, hide them again
        buttons[i1][j1].config(text="", state="normal")
        buttons[i2][j2].config(text="", state="normal")

    # Reset the choices
    first_choice = None
    second_choice = None
