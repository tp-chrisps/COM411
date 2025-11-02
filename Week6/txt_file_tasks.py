import os
def cwd():
    filepath = os.getcwd()
    print(f"The current working directory is: {filepath}")
    print(f"The directory contains the following files:{os.listdir(filepath)}")

def run():
    cwd()

run()