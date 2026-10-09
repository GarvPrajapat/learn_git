water = 1000
water += int(input("Enter the incoming water in liters :"))
water -= int(input("Enter the removed water in liters :"))

print(f"4 tanks, every tank cantain : {water/4:.2f}")