import random as rand

num,choice,attemps = rand.randint(1,1000),0,0
print(num)

while num != choice :
    choice = int(input("Enter your Guess : "))
    if num > choice :
        print("\nto low",end="")
    else:
        print("\nto high",end="")
    attemps+=1 

print(f"\rBingo the you guessed number in {attemps}")