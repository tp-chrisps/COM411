phone:int = 0
while phone ==0:
    look = input("\nWhere should i look?\nbedroom?\nliving room?\nbathroom?")
    if look == "bedroom":
        look = input("where in the bedroom should i look?")
        if look == "bed": print("Found some shows but no phones")
        else:print("Found some mess but no phone")
    elif look == "living room":
        look = input("where in the living room should i look?\ntable?\nsofa?\ncupboard?")
        if look == "table":
            print("Yes! I found me phone!")
            phone = 1
        else:print("Found some stuff but no phone")
    elif look == "bathroom":
        look = input("where in the bathroom should i look?\nbath?\ncabinet?")
        if look == "bath":print("Found a rubber duck but no phone")
        else: print("Found some stuff but no phone")
    else: print("I dont know where that is but I will keep looking.")



