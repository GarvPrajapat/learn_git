marks1 = int(input("Enter the makrs of 1st subject : "))
marks2 = int(input("Enter the makrs of 2nd subject : "))
marks3 = int(input("Enter the makrs of 3rd subject : "))

total = marks1 + marks2 + marks3
percent = total/3

if percent >= 90:
    print("Grade A")
elif percent >= 80:
    print("Grade B")
elif percent >= 70:
    print("Grade C")
elif percent >= 60:
    print("Grade D")
else:
    print("Grade f")