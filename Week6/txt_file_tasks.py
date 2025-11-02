import os
def cwd():
    filepath = os.getcwd()
    print(f"The current working directory is: {filepath}")
    print(f"The directory contains the following files:{os.listdir(filepath)}")

def display_chars(path, num):
    with open(path) as file:
        data = file.read(num)
    print(data)
    file.close()

def display_line(path):
    with open(path) as file:
        data = file.readline()
    print(data)
    file.close()

def display_text(path):
    with open(path) as file:
        data = file.read()
    print(data)
    file.close()

def search(path):
    print("Searching...")
    with open(path) as file:
        data = file.readlines()
    for line in data:
        print(f"Looked in {line}")
    print("...Done!")

def search_books(path):
    print("Searching...")
    sections = ""
    books = "Books:\n"
    with open(path) as file:
        data = file.readlines()
    for line in data:
        if line[:7] == "Section":
            sections = sections + line
        else:
            books = books + line
    file.close()
    file = open("section-books.txt","w")
    file.write(f"{sections}\n\n{books}")
    print("Done!")
    print(f"{sections}\n\n{books}")


def run():
    cwd()

def run_task2():
    path = "library.txt"
    display_chars(path, 5)
    display_line(path)
    display_text(path)

def run_task3():
    path = "library.txt"
    search(path)

def run_task4():
    path = "books.txt"
    search_books(path)

if __name__ == "__main__":
    run_task4()