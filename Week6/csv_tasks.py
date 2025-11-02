def read_csv(path):
    with open(path) as file:
        data = file.readlines()
    print(f"Headings:\n{data[0]}")
    print("Values:")
    for line in data[1:]:
        print(line)

if __name__ == "__main__":
    read_csv("clothing.csv")