import random as rand

num,choice,attemps = rand.randint(1,1000),0,0

while num != choice :
    choice = int(input("Enter your Guess : "))

    if num > choice :
        print("to low")
    else:
        print("to high")
    attemps+=1
    
print(f"Bingo the you guessed number in {attemps}")