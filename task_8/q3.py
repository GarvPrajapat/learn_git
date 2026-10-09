num = "6376242334"

if len(num) == 10 and num.isnumeric() and num[0] in "6789" :
    print("valid phone number ")
else:
    print("invalid phone number ")