def read_csv(path):
    with open(path) as file:
        data = file.readlines()
    print(f"Headings:\n{data[0]}")
    print("Values:")
    for line in data[1:]:
        print(line)

def extract(path):
    names = ""
    with open(path) as file:
        data = file.readlines()
    for line in data:
        names = names + line.split(",")[1] + "\n"
    print("Done! The extracted items are as follows:")
    print(names)

def export(path, num):
    for i in range(num):
        id = input("Enter item_id: ")
        item = input("Enter item_name: ")
        colour = input("Enter item_colour: ")
        with open(path, "a") as file:
            file.write(f"{id},{item},{colour}\n")
    print("Done!")

if __name__ == "__main__":
    export("exported_items.csv",2)