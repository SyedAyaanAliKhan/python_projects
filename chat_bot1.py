# Define a function to greet the user
def greet():
    print("Hi there! I'm ChatBot.")
    print("What's your name?")

# Define a function to bid farewell to the user
def farewell(name):
    print(f"Nice chatting with you, {name}! Goodbye.")

# Main function where the conversation happens
def main():
    greet()  # Call greet function to start the conversation
    name = input("Enter your name: ")  # Ask user for their name
    print(f"Hello, {name}!")  # Greet the user by their name

    # Conversation loop
    while True:
        message = input("You: ").lower()  # Get user input and convert to lowercase

        # Respond based on user input
        if message == "hi" or message == "hello":
            print("ChatBot: Hi there!")
        elif message == "how are you":
            print("ChatBot: I'm good, thank you!")
        elif message == "what's your favorite color":
            print("ChatBot: I don't have a favorite color. What's yours?")
        elif message == "bye":
            farewell(name)  # Call farewell function to say goodbye
            break  # Exit the loop and end the conversation
        else:
            print("ChatBot: Sorry, I didn't understand that.")  # Default response for unrecognized input

if __name__ == "__main__":
    main()  # Call the main function to start the chat bot
