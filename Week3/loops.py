count = input("How many obstacles must I avoid?")
num = 0
while int(count) > 0:
    print("Avoiding...",end="")
    num = num + 1
    print(f"Done! {num} obstacles avoided!")
    count = int(count) - 1
print("All obstacles have been avoided")
