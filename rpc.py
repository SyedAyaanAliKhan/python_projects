import random

# List of choices
choices = ["rock", "paper", "scissors"]

# Get the user's choice
print("Choose one: Rock, Paper, Scissors")
user_choice = input().lower()

# Validate the user's choice
if user_choice not in choices:
    print("Invalid choice! Please choose Rock, Paper, or Scissors.")
else:
    # Computer's random choice
    computer_choice = random.choice(choices)

    # Show choices
    print(f"You chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("Computer wins!")
