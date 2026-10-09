balance = 5000
balance += int(input("Enter the Deposit amount : "))
balance -= int(input("Enter the withdraw amount : "))
balance += balance * 0.5
print(f"final balance : {balance}")