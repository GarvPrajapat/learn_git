weight = float(input("Enter the weight : "))
height = float(input("Enter the height : "))
bmi = weight / (height*height)

if bmi >= 30 :
    print(f"{bmi}, obesity")
elif bmi>=25 : 
    print(f"{bmi}, overweight")
elif bmi>=18.5 : 
    print(f"{bmi}, Normal weight")
else :
    print(f"{bmi}, Underweight")