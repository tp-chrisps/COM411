# display message to the screen
age = int(input("Enter your age: "))
height = int(input("Enter your height: "))/100
weight = int(input("Enter your weight: "))
bmi = weight / (height * height)
if bmi < 18.5: print("You are under weight")
if bmi >= 18.5 and bmi < 25: print("You are heathly weight")
if bmi >= 25 and bmi < 30: print("you are obese weight")
if bmi >= 40: print("You are very obese weight")
print("Your BMI is", bmi)
