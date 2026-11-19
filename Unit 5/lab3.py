import random

while True:
    print("\n--- Dice Simulator ---")
    print("1. Roll Dice")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        dice = random.randint(1, 6)
        print("You rolled:", dice)

    elif choice == "2":
        print("Exiting Dice Simulator")
        break

    else:
        print("Invalid choice")