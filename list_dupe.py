def find_duplicates(numbers):
    # Convert the list to a set to remove duplicates, then compare lengths
    seen = set()
    duplicates = set()
    
    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)
    
    return list(duplicates)

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
    
    # Find duplicates
    duplicates = find_duplicates(numbers)
    
    if duplicates:
        print("Duplicate numbers found:", duplicates)
    else:
        print("No duplicates found.")

if __name__ == "__main__":
    main()
