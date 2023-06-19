import tkinter as tk
import random
from tkinter import messagebox

# Create the Tic Tac Toe board
board = [' ' for _ in range(9)]

# Winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

# Function to check if a player has won
def check_win(player):
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to handle a player's move
def handle_move(button, position):
    if board[position] == ' ':
        button.config(text=current_player)
        board[position] = current_player

        if check_win(current_player):
            messagebox.showinfo("Game Over", f"{current_player} wins!")
            reset_game()
        elif ' ' not in board:
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            change_turn()

# Function to change the turn
def change_turn():
    global current_player
    current_player = 'O' if current_player == 'X' else 'X'

    if current_player == 'O' and game_mode == "Computer":
        computer_move()

# Function for the computer's move
def computer_move():
    available_moves = [i for i in range(9) if board[i] == ' ']
    move = random.choice(available_moves)
    buttons[move].config(text=current_player)
    board[move] = current_player

    if check_win(current_player):
        messagebox.showinfo("Game Over", f"{current_player} wins!")
        reset_game()
    elif ' ' not in board:
        messagebox.showinfo("Game Over", "It's a tie!")
        reset_game()
    else:
        change_turn()

# Function to reset the game
def reset_game():
    global current_player
    current_player = 'X'
    for i in range(9):
        board[i] = ' '
        buttons[i].config(text=' ')

# Function to handle game mode selection
def select_game_mode(mode):
    global game_mode
    game_mode = mode
    reset_game()
    if game_mode == "Computer" and current_player == 'O':
        computer_move()

# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe")

# Create the buttons for the board
buttons = []
for i in range(3):
    for j in range(3):
        button = tk.Button(window, text=' ', font=('Arial', 20), width=8, height=3,
                          command=lambda position=i*3+j: handle_move(buttons[position], position))
        button.grid(row=i, column=j, padx=5, pady=5)
        buttons.append(button)

# Create the game mode selection buttons
mode_label = tk.Label(window, text="Select Game Mode:", font=('Arial', 14))
mode_label.grid(row=3, column=0, columnspan=3, pady=10)  # Span three columns

two_players_button = tk.Button(window, text="Two Players", font=('Arial', 12),
                              command=lambda: select_game_mode("Two Players"))
two_players_button.grid(row=4, column=0, columnspan=3, pady=5, sticky='nsew')  # Span three columns, align center

computer_button = tk.Button(window, text="Play against the Computer", font=('Arial', 12),
                            command=lambda: select_game_mode("Computer"))
computer_button.grid(row=5, column=0, columnspan=3, pady=5, sticky='nsew')  # Span three columns, align center


# Set the initial game mode and current player
game_mode = "Two Players"
current_player = 'X'

# Start the game
window.mainloop()