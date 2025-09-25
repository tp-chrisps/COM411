# display message to the screen

lives = input("enter number of lives")
while not lives.isdigit(): lives = input("enter valid number of lives")

energy = input("enter number of energy levels")
while not energy.isdigit(): energy = input("enter valid number of energy levels")

shield = input("enter number of shields")
while not shield.isdigit(): shield = input("enter valid number of shields")

print("health has been set")

heart = ("♥")
energyIcon=("♦")
shieldIcon=("✠")
print("\nLives:", end=(" "))
for i in range(0, int(lives)):
    print(heart, end="")
print("\nEnergy:", end=(" "))
for i in range(0, int(energy)):
    print(energyIcon, end="")
print("\nShield:", end=(" "))
for i in range(0, int(shield)):
    print(shieldIcon, end="")

