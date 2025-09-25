# display message to the screen
lives = int(input("enter number of lives"))
energy = int(input("enter number of energy levels"))
shield = int(input("enter number of shields"))
print("health has been set\n\n")

heart = ("♥")
energyIcon=("♦")
shieldIcon=("✠")
print("\nLives:", end=(" "))
for i in range(0, lives):
    print(heart, end="")
print("\nEnergy:", end=(" "))
for i in range(0, energy):
    print(energyIcon, end="")
print("\nShield:", end=(" "))
for i in range(0, shield):
    print(shieldIcon, end="")

