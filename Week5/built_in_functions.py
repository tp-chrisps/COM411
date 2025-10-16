print("Program Started!")
char = input("Enter a character: ")
while len(char) != 1:
    print("Error enter a single digit character")
    char = input("Enter a character: ")
print(f"The ASCII code for {char} is {ord(char)}")
print("Program Ended!")