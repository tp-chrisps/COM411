import random as rnd
def prime (num):
    count = 0
    for i in range(2, round(num/2)):
        if num % i == 0:
            count =+ 1
    if count == 0:
        return True
    else: return False

num = int(input("Enter a number: "))
print(prime(num))
