n1 = int(input("Enter the 1st number : "))
n2 = int(input("Enter the 2nd number : "))
n3 = int(input("Enter the 3rd number : "))

max = n1 if n1>n2 and n1>n3 else n2 if n2 > n3 else n3
print(f"the Greatest among all of them is : {max}")