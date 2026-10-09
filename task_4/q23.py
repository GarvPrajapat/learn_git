balance = 10000
withdraw = int(input("enter the withdrow ammount : "))

if withdraw > 0 and withdraw < balance :
    print(f"current amount : {balance - withdraw}")
else:
    print("insufficient balance or invalid ammount ")