def main():
    # Prompt the user for input
    input_string = input("Enter numbers separated by spaces: ")
    
    # Convert the input string to a list of integers
    try:
        numbers = list(map(int, input_string.split()))
    except ValueError:
        print("Please enter only numbers.")
        return
    
    if not numbers:
        print("No numbers entered.")
        return
    
    # Sort the list
    numbers.sort()
    
    # Display the sorted list
    print("Sorted numbers:", numbers)

if __name__ == "__main__":
    main()
