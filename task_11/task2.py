products = [
    {"name": "Ball", "price": 5, "quantity": 100},
    {"name": "Fountain", "price": 50, "quantity": 100},
    {"name": "Roller", "price": 20, "quantity": 100},
    {"name": "Parker", "price": 100, "quantity": 100},
    {"name": "Gel", "price": 10, "quantity": 100},
]

user_products = {}

while True:
    print("1. Add Products.")
    print("2. Update Products.")
    print("3. Remove Products.")
    print("4. View Inventory.")
    print("5. Search Products.")
    print("6. Total Price.")
    print("7. Exit Program.")

    choice = input("Enter your choice: ")

    if choice == "1":
        pen_type = input("Enter the type of Pen (first letter capital): ")

        index = None
        for i in range(len(products)):
            if products[i]["name"] == pen_type:
                index = i
                break
        else:
            print("\nInvalid Pen type...\n")
            continue

        quantity = int(input(f"How many {pen_type} pens do you want? "))

        if quantity <= 0:
            print("Enter a quantity greater than zero.")
        elif products[index]["quantity"] >= quantity:
            products[index]["quantity"] -= quantity

            if pen_type in user_products:
                user_products[pen_type][1] += quantity
            else:
                user_products[pen_type] = [products[index]["price"], quantity]

            print(f"{quantity} {pen_type} pen(s) added to your cart.")
        else:
            print("Not enough stock.")

    elif choice == "2":
        pen_type = input(
            "Enter the type of Pen in which you want to make changes (first letter capital): "
        )

        if pen_type not in user_products:
            print("Product doesn't exist in cart...")
            continue

        quantity = int(input("How many more pens do you want to add? "))

        if quantity <= 0:
            print("Enter a quantity greater than zero.")
            continue

        index = None
        for i in range(len(products)):
            if products[i]["name"] == pen_type:
                index = i
                break

        if products[index]["quantity"] >= quantity:
            products[index]["quantity"] -= quantity
            user_products[pen_type][1] += quantity
            print(f"{pen_type} quantity updated.")
        else:
            print("Not enough stock.")

    elif choice == "3":
        pen_type = input("Enter the type of Pen to remove (first letter capital): ")

        if pen_type not in user_products:
            print("Product doesn't exist in cart...")
            continue

        for item in products:
            if item["name"] == pen_type:
                item["quantity"] += user_products[pen_type][1]
                break

        del user_products[pen_type]
        print(f"{pen_type} removed from your cart.")

    elif choice == "4":
        print("*-" * 20)
        for item in products:
            print(
                f"Pen Type: {item['name']}, "
                f"Price: {item['price']}, "
                f"Quantity available: {item['quantity']}"
            )
        print("*-" * 20)

    elif choice == "5":
        pen_type = input("Enter the type of Pen to search for (first letter capital): ")

        for item in products:
            if item["name"] == pen_type:
                print(
                    f"Pen Type: {item['name']}, "
                    f"Price: {item['price']}, "
                    f"Quantity available: {item['quantity']}"
                )
                found = True
                break
        else:
            print("Product not found.")

    elif choice == "6":
        total = 0
        print("-" * 30)

        if not user_products:
            print("Your cart is empty.")
        else:
            for pen_type, value in user_products.items():
                amount = value[0] * value[1]
                print(f"{pen_type} Pens: {value[1]} X {value[0]} = {amount}")
                total += amount

        print("-" * 30)
        print(f"Total Bill: {total}")
        print("-" * 30)

    elif choice == "7":
        print("\nExiting the program...")
        break

    else:
        print("\nInvalid choice.\n")
