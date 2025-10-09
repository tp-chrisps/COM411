bars = int(input("How many bars should be charged?"))
bar = "█"
ba = "█"
for i in range(bars):
    print(f"Charging: {bar}")
    bar = f"{bar}{ba}"
print("The battery is fully charged")