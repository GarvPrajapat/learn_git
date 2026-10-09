user_name = input("Enter your username : ")
password = input("Enter your password : ")
age = int(input("Enter your age : "))
salary = int(input("Enter your salary : "))

if age >= 18 and salary > 50000 :
    if user_name == "Manager" and password == "password":
        print("Account verified")
    else:
        print("Account doesn't exist")
else:
    print("your age or salary doesn't match with creditanils")