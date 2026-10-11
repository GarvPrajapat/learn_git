products = [
    {"name": "ball", "price": 5, "quantity": 100},
    {"name": "Fountain", "price": 50, "quantity": 100},
    {"name": "Roller", "price": 20, "quantity": 100},
    {"name": "Parker", "price": 100, "quantity": 100},
    {"name": "gel", "price": 10, "quantity": 100},
]

user_products = {}

while True:

    print(f"1. Add Products.")
    print(f"2. Update Products.")
    print(f"3. Remove Products.")
    print(f"4. View Inventory.")
    print(f"5. Search Products.")
    print(f"6. Total Price.")
    print(f"7. Exit Program.")
    choice = input("Enter your choice : ")

    if choice == "1":
        ...
    elif choice == "2":
        ...
    elif choice == "3":
        ...
    elif choice == "4":
        ...
    elif choice == "5":
        ...
    elif choice == "6":
        ...
    elif choice == "7":
        print(f"\nExiting the Prgram...")
        break
    else :
        print("\nInvalid Choice..\n")