import random

# Sample questions for different difficulty levels
questions = {
    "easy": [
        {"question": "What is 2 + 2?", "choices": ["3", "4", "5", "6"], "answer": "4"},
        {"question": "What is the capital of France?", "choices": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"}
    ],
    "medium": [
        {"question": "What is 12 * 12?", "choices": ["144", "122", "130", "156"], "answer": "144"},
        {"question": "Which planet is known as the Red Planet?", "choices": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"}
    ],
    "hard": [
        {"question": "What is the square root of 256?", "choices": ["16", "14", "18", "20"], "answer": "16"},
        {"question": "What is the chemical symbol for Gold?", "choices": ["Au", "Ag", "Pb", "Fe"], "answer": "Au"}
    ]
}

# Function to choose difficulty
def choose_difficulty():
    print("Choose difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = input("Enter the number corresponding to the difficulty level: ")
    if choice == '1':
        return "easy"
    elif choice == '2':
        return "medium"
    elif choice == '3':
        return "hard"
    else:
        print("Invalid choice. Defaulting to Easy.")
        return "easy"

# Function to get number of tries based on difficulty
def get_tries(difficulty):
    if difficulty == "easy":
        return 3
    elif difficulty == "medium":
        return 2
    elif difficulty == "hard":
        return 1

# Function to run the quiz
def run_quiz():
    difficulty = choose_difficulty()
    tries = get_tries(difficulty)
    questions_list = questions[difficulty]
    
    random.shuffle(questions_list)  # Shuffle questions to ensure randomness

    for q in questions_list:
        print("\n" + q["question"])
        for idx, choice in enumerate(q["choices"], 1):
            print(f"{idx}. {choice}")

        for attempt in range(tries):
            answer = input("Your answer (enter the number): ")
            if answer.isdigit() and 1 <= int(answer) <= len(q["choices"]):
                if q["choices"][int(answer) - 1] == q["answer"]:
                    print("Correct!")
                    break
                else:
                    if attempt < tries - 1:
                        print("Incorrect. Try again.")
                    else:
                        print(f"Sorry, the correct answer was '{q['answer']}'.")
            else:
                print("Invalid input. Please enter a number corresponding to one of the choices.")

    print("\nQuiz completed!")

# Run the quiz
if __name__ == "__main__":
    run_quiz()
