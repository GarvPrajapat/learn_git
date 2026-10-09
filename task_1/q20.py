hour = int(input("Enter the hour :"))
min = int(input("Enter the min :"))
sec = int(input("Enter the sec :"))

min += hour*60
sec += min*60

print(f"total seconds = {sec}")