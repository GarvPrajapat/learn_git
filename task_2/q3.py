amount = int(input("Enter the prize of 1st product : "))
amount += int(input("Enter the prize of 2nd product : "))
amount += int(input("Enter the prize of 3rd product : "))
gst = amount * 0.18
amount -= (amount * 0.10) - gst

print(f"total : {amount}")