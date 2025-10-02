i = 0

num1 = input("enter first number")
num2 = input("enter second number")
num3 = input("enter third number")
if (int(num1) % 2)==0: i = i + 1
if (int(num2) % 2)==0: i = i + 1
if (int(num3) % 2)==0: i = i + 1
print(f"There were {i} even and {3-i} odd numbers")