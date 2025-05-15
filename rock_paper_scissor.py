import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk  # You might need to install Pillow

# Create the main window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x400")

# Load images
rock_img = ImageTk.PhotoImage(Image.open("rock.jpg").resize((80, 80)))
paper_img = ImageTk.PhotoImage(Image.open("paper.webp").resize((80, 80)))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((80, 80)))

choices = ["rock", "paper", "scissors"]

# Label to show the result
result_label = tk.Label(window, text="", font=("Arial", 16))
result_label.pack(pady=20)

# Function to decide the winner
def play(player_choice):
    computer_choice = random.choice(choices)
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result = f"You win! Computer chose {computer_choice}."
    else:
        result = f"You lose! Computer chose {computer_choice}."

    result_label.config(text=result)

# Buttons with images
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, image=rock_img, command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, image=paper_img, command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, image=scissors_img, command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Run the main event loop
window.mainloop()
