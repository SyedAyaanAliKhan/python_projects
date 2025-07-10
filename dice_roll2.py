import tkinter as tk
from tkinter import messagebox
import random

dice_faces = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

class DiceGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎲 Dice Race to 12 🎲")
        self.root.geometry("400x350")
        self.root.configure(bg="#f0f0f0")

        self.p1_score = 0
        self.p2_score = 0
        self.turn = 1

        tk.Label(root, text="🎯 Race to 12!", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=10)

        self.score_label = tk.Label(root, text=self.get_score_text(), font=("Helvetica", 12), bg="#f0f0f0")
        self.score_label.pack()

        self.dice_label = tk.Label(root, text=dice_faces[0], font=("Helvetica", 100), fg="#333", bg="#f0f0f0")
        self.dice_label.pack(pady=10)

        self.turn_label = tk.Label(root, text="Player 1's turn", font=("Helvetica", 12), bg="#f0f0f0")
        self.turn_label.pack()

        self.info_label = tk.Label(root, text="👉 Right-click to roll the dice", font=("Helvetica", 10), bg="#f0f0f0", fg="gray")
        self.info_label.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game,
                                      font=("Helvetica", 10), bg="#f44336", fg="white")
        self.reset_button.pack(pady=5)

        # Bind right-click to roll
        self.root.bind("<Button-3>", self.on_right_click)

        self.rolling = False  # to avoid rolling multiple times

    def get_score_text(self):
        return f"Player 1: {self.p1_score}    Player 2: {self.p2_score}"

    def on_right_click(self, event):
        if not self.rolling:
            self.roll_dice()

    def roll_dice(self):
        self.rolling = True
        self.animate_roll(10)

    def animate_roll(self, count):
        if count > 0:
            face = random.randint(0, 5)
            self.dice_label.config(text=dice_faces[face])
            self.root.after(80, self.animate_roll, count - 1)
        else:
            rolled = random.randint(1, 6)
            self.dice_label.config(text=dice_faces[rolled - 1])
            self.update_score(rolled)

    def update_score(self, rolled):
        if self.turn == 1:
            self.p1_score += rolled
            if self.p1_score >= 12:
                messagebox.showinfo("Game Over", "🎉 Player 1 wins!")
                self.reset_game()
                return
            self.turn = 2
        else:
            self.p2_score += rolled
            if self.p2_score >= 12:
                messagebox.showinfo("Game Over", "🎉 Player 2 wins!")
                self.reset_game()
                return
            self.turn = 1
        self.score_label.config(text=self.get_score_text())
        self.turn_label.config(text=f"Player {self.turn}'s turn")
        self.rolling = False

    def reset_game(self):
        self.p1_score = 0
        self.p2_score = 0
        self.turn = 1
        self.rolling = False
        self.score_label.config(text=self.get_score_text())
        self.turn_label.config(text="Player 1's turn")
        self.dice_label.config(text=dice_faces[0])

if __name__ == "__main__":
    root = tk.Tk()
    game = DiceGame(root)
    root.mainloop()
