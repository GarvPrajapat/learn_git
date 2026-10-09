perfect = int(input("Enter the num : "))
res = 0
for i in range(1,perfect):
    if not perfect%i :
        res+=i
if res == perfect:
    print(f"{perfect} is a perfect number.")
else:
    print(f"{perfect} is not a perfect number.")