products = [
    {'name': "Ball", 'price': 5, 'quantity': 100},
    {'name': "Fountain", 'price': 50, 'quantity': 100},
    {'name': "Roller", 'price': 20, 'quantity': 100},
    {'name': "Parker", 'price': 100, 'quantity': 100},
    {'name': "Gel", 'price': 10, 'quantity': 100},
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
        type = input(f"Enter the type of Pen (first letter capital): ")
        index = None
        for i in range(len(products)):
            if products[i]['name'] == type.title():
                index = i
                break
        else:
            print(f"\nInvalid Pen type...\n")
            continue
        quant = int(input(f"How many {type} Pens You want : "))
        if (products[index]['quantity'] - quant) >= 0:
            products[index]['quantity'] -= quant
            user_products[type] = (products[index]['price'],quant)
        else :
            print(f"Not enough Stock")

    elif choice == "2":
        ...

    elif choice == "3":
        ...

    elif choice == "4":
        print("*-"*20)
        for item in products:
            print(f"Pen Type : {item['name']}, Price : {item['price']}, Quantity available : {item['quantity']}")
        print("*-"*20)
    elif choice == "5":
        ...

    elif choice == "6":
        total = 0
        print("-"*20)
        for key,value in user_products.items():
            print(f"{key} Pens : {quant} Quantity => {value[0] * value[1]} amount")
            total += value[0] * value[1]
        print("-"*20)
        print(f"Total Bill : {total}")
        print("-"*20)

    elif choice == "7":
        print(f"\nExiting the Prgram...")
        break
    else :
        print("\nInvalid Choice..\n")
