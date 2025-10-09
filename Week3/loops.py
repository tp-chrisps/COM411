word = input("What phrase do you want to see in reverse?\n")
print("Reversing...")
print("The phrase is: ",end="")
for i in range(len(word)):
    print(word[(len(word)-1)-i],end="")
