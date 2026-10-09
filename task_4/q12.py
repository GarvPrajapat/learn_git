user_name = input("Enter your user name : ")
user_pass = input("Enter your pin : ")

if user_name == "admin" and user_pass == "cat":
    print("login success")
else:
    print("not valid crediantals")