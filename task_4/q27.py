temp = int(input("Enter the temperature : "))
humi = int(input("Enter the hummidity : "))

if temp > 40 and humi > 60 :
    print("very high temperature ")
elif temp > 20 and humi > 30 :
    print("normal temperature ")
else:
    print("good temperauture")