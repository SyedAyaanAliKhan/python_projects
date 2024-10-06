# Grocery Store Program

grocery_items = {
    "apple": 200,
    "banana": 180,
    "carrot": 50,
    "milk": 200,
    "bread": 150,
    "eggs": 250,
    "chicken": 400
}

def display_items():
    print("\nWelcome to e-grocers here are the available items:")
    for item, price in grocery_items.items():
        print(f"{item.title()}: ₹{price:.2f}")

def main():
    selected_items = {}
    total_price = 0.0
    
    while True:
        display_items()
        choice = input("\nEnter the item you want to buy (type 'done' if finished): ").lower()
        
        if choice == 'done':
            break
        elif choice in grocery_items:
            quantity = int(input(f"How many {choice}s do you want to buy? "))
            selected_items[choice] = selected_items.get(choice, 0) + quantity
            total_price += grocery_items[choice] * quantity
            print(f"{quantity} {choice}(s) added to your cart.")
        else:
            print("Item not available. Please choose a valid item.")

    # Generate receipt
    if selected_items:
        print("\n--- Receipt ---")
        for item, quantity in selected_items.items():
            item_price = grocery_items[item] * quantity
            print(f"{quantity} x {item.title()}: ₹{item_price:.2f}")
        print(f"Total Price: ₹{total_price:.2f}")
    else:
        print("No items selected.")

if __name__ == "__main__":
    main()
