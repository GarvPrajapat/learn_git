cars = [
    {
        'name' : "Swift",
        'ID' : 1,
        'avail' : True
    },
    {
        'name' : "Swift",
        'ID' : 2,
        'avail' : False
    },
    {
        'name' : "Swift",
        'ID' : 3,
        'avail' : True
    },
]

while(True):
    print(f"1. Show Cars")
    print(f"2. Rent Car")
    print(f"3. Return Car")
    print(f"4. Exit the program")
    choice = input(f"Enter Your choice : ")


    if choice == "1":
        print('-'*20)
        for car in cars:
            if car['avail']:
                print(f"|-> Name : {car['name']}")
                print(f"|-> Id : {car['ID']}")
                print(f"|-> Is Available : {car['avail']}")
                print('-'*20)

    elif choice == "2":
        car_id = int(input("Enter the Car ID : "))
        for car in cars:
            if car_id == car['ID'] and car['avail']:
                print("\nCar is available and assigning to you\n")
                car['avail'] = False
                break
        else :
            print("\nCar is not available\n")
            
    elif choice == "3":
        car_id = int(input("Enter the Car ID : "))
        for car in cars:
            if car_id == car['ID'] and not car['avail']:
                print("\nTaking car back.\n")
                car['avail'] = True
                break
        else :
            print("\nCar not found in data\n")

    elif choice == "4":
        print(f"\nExiting the program. \n")
        break
    else:
        print("\nInvalid chocice. \n")