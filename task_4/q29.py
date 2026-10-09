num1 = int(input("Enter your 1st number : "))
num2 = int(input("Enter your 2nd number : "))
symbol = input("Enter the symbol of operation : ")

if symbol == "+":
    print(num1 + num2)
elif symbol == "-":
    print(num1 - num2)
elif symbol == "*":
    print(num1 * num2)
elif symbol == "/":
    print(num1 / num2)
elif symbol == "//":
    print(num1 // num2)
elif symbol == "%":
    print(num1 % num2)
elif symbol == "**":
    print(num1 ** num2)
else:
    print("envalid operator")