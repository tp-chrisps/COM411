import os
def cwd():
    filepath = os.getcwd()
    print(f"The current working directory is: {filepath}")
    print(f"The directory contains the following files:{os.listdir(filepath)}")

def display_chars(path, num):
    with open("library.txt") as file:
        data = file.read(num)
    print(data)
    file.close()

def display_line(path):
    with open("library.txt") as file:
        data = file.readline()
    print(data)
    file.close()

def display_text(path):
    with open("library.txt") as file:
        data = file.read()
    print(data)
    file.close()

def run():
    cwd()

def run_task2():
    path = "library.txt"
    display_chars(path, 5)
    display_line(path)
    display_text(path)

if __name__ == "__main__":
    run_task2()