num = int(input("How far are we from the target? "))

for i in range(num):
    print(f"{num - i} steps remaining")
print("Target achieved!")