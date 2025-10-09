level = int(input("What level of brightness is required? "))
print("Adjusting brightness")
a = "**"
b = "**"
for i in range(0,level,2):
    print("Brightness level: ",end="")
    print(a)
    a = a + b
print("Complete!")
