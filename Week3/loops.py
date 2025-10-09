word = input("What word do you see?\n")
print("Displaying index positions")
for index in range(len(word)):
    print(f"index {index}, {word[index]}")