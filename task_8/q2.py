pan = "1234567890"

if len(pan) == 10 and pan[:5].isupper() and pan[5:9].isnumeric() and pan[-1].isupper():
    print("valid pan number")
else : 
    print("invalid pan number")