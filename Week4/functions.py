import random as rnd
def add (a,b):
    c = a + b
    return c
a = rnd.randint(1,10)
b = int(input())
ans = add(a,b)
print(ans)