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

if __name__ == "__main__":
    extract("clothing.csv")