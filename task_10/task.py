data = []

while True:
    print(f"1. Insert Student info ")
    print(f"2. View info ")
    print(f"3. Exit ")
    choice = input(f"Enter Your Choice : ")

    if choice == '1':
        stu_data = {}
        stu_data['name'] = input("\nEnter Student Name : ")
        stu_data['python'] = int(input("Enter the marks of python : "))
        stu_data['cpp'] = int(input("Enter the marks of C++ : "))
        stu_data['java'] = int(input("Enter the marks of Java : "))

        if stu_data['python'] > 100 or stu_data['cpp'] > 100 or stu_data['java'] > 100 :
            print("\nInvalid marks entry",end=f"\n{'-*'*15}\n")
            continue

        stu_data['percent'] = (stu_data['python'] + stu_data['cpp'] + stu_data['java']) * 0.3
        data.append(stu_data)
        print(f"\n-> Student detail added to data.\n",end=f"{'-*'*15}\n")

    elif choice == '2':
        print('-*'*15)
        for student in data:
            print(
f'''|\n|-> Name    : {student['name']}
|-> Python  : {student['python']}
|-> C++     : {student['cpp']}
|-> Java    : {student['java']}
|-> Percent : {student['percent']:.2f} 
|\n{'-*'*15}''',end='')
        print()
            
    elif choice == '3':
        print('-*'*15)
        for student in data:
            print(
f'''|\n|-> Name    : {student['name']}
|-> Python  : {student['python']}
|-> C++     : {student['cpp']}
|-> Java    : {student['java']}
|-> Percent : {student['percent']:.2f} 
\n{'-*'*15}''',end='')
        print("exiting the program...")
        break
    else:
        print("\nInvalid Choice\n")