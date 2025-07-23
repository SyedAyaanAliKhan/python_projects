import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic Tac Toe")

current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

def check_winner():
    # Rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    # Tie
    if all(board[i][j] != "" for i in range(3) for j in range(3)):
        return "Tie"
    return None

def on_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled")
        winner = check_winner()
        if winner:
            if winner == "Tie":
                messagebox.showinfo("Tic Tac Toe", "It's a Tie!")
            else:
                messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_board():
    global current_player
    current_player = "X"
    for i in range(3):
        for j in range(3):
            board[i][j] = ""
            buttons[i][j].config(text="", state="normal")

# Create 3x3 buttons
for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text="", width=10, height=4,
                        font=("Arial", 24),
                        command=lambda i=i, j=j: on_click(i, j))
        btn.grid(row=i, column=j)
        buttons[i][j] = btn

root.mainloop()
