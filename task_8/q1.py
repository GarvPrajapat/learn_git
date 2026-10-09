num = "423456789123"

if len(num) == 12 and num.isnumeric() and num[0] not in "01" :
    print("valid aadhaar")
else :
    print("invalid aadhaar")