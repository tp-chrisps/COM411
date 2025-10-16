print("Program Started!")
code = int(input("Please enter an ASCII code"))
while code < 1:
    code = int(input("Error \nPlease enter an ASCII code:"))
if code in range(32, 127):
    print(f"The character represented by the ASCII code is: {chr(code)}")
print("Program Ended!")