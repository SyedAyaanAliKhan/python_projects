import random

def get_computer_choice():
    """Function to randomly choose Rock, Paper or Scissors for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    """Function to get user's choice of Rock, Paper or Scissors."""
    while True:
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid input. Please choose rock, paper, or scissors.")

def determine_winner(user_choice, computer_choice):
    """Function to determine the winner of the game."""
    if user_choice == computer_choice:
        return 'draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'user'
    else:
        return 'computer'

def main():
    user_score = 0
    computer_score = 0
    rounds = 5 

    print("Welcome to Rock, Paper, Scissors game!")
    
    for _ in range(rounds):
        print("\n--- New Round ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == 'user':
            print("You win this round!")
            user_score += 1
        elif winner == 'computer':
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("This round is a draw!")

    print("\n--- Final Scores ---")
    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")

    if user_score > computer_score:
        print("Congratulations! You win the game!")
    elif user_score < computer_score:
        print("Sorry, Computer wins the game!")
    else:
        print("It's a tie game!")

if __name__ == "__main__":
    main()
