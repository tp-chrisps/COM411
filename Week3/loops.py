i = int(input("How many numbers should I add up?"))
count = 0
for j in range (1,i+1):
    num = int(input(f"Enter a number {j} of {i}: "))
    count = count + num
print(f"The answer is {count}")