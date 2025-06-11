import tkinter as tk
import random

score = 0

def roll_dice():
    global score
    guess = guess_entry.get()
    if not guess.isdigit() or int(guess) not in range(1, 7):
        result_label.config(text="Enter a number between 1 and 6")
        return
    roll = random.randint(1, 6)
    if int(guess) == roll:
        score += 1
        result_label.config(text=f"Correct! Dice: {roll} | Score: {score}")
    else:
        result_label.config(text=f"Wrong! Dice: {roll} | Score: {score}")

root = tk.Tk()
root.title("Dice Guessing Game")
root.geometry("300x200")

title_label = tk.Label(root, text="Guess the Dice Roll (1-6)")
title_label.pack(pady=10)

guess_entry = tk.Entry(root)
guess_entry.pack()

roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
