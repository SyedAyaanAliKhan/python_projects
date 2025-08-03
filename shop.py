import time

items = {
    "apple": 20,
    "banana": 10,
    "milk": 50,
    "bread": 30,
    "eggs": 5,
    "rice": 60,
    "chocolate": 40
}

cart = {}

print("=" * 40)
print("   WELCOME TO PYTHON GROCERY STORE   ")
print("=" * 40)
print("Available items:")
for item, price in items.items():
    print(f"{item.capitalize():10} - ₹{price}")
print("=" * 40)

while True:
    choice = input("Enter item to buy (or 'done' to finish): ").lower()
    if choice == "done":
        break
    if choice in items:
        qty = int(input("Enter quantity: "))
        if choice in cart:
            cart[choice] += qty
        else:
            cart[choice] = qty
        print(f"Added {qty} x {choice} to your cart.")
    else:
        print("Item not available. Try again!")

print("\nGenerating your bill...\n")
time.sleep(1)
print("=" * 40)
print("           PYTHON GROCERY BILL        ")
print("=" * 40)
total = 0
for item, qty in cart.items():
    price = items[item] * qty
    total += price
    print(f"{item.capitalize():10} x {qty:<3} = ₹{price}")
print("-" * 40)
print(f"TOTAL AMOUNT{' ':16}₹{total}")
print("=" * 40)
print("Thank you for shopping with us! 🛒")
print("=" * 40)
