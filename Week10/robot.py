class Robot:
    MAX_ENERGY = 100
    def __init__(self, name, age, energy):
        self.name = name
        self.age = age
        self.energy = energy

    def display(self):
        print(f"I am {self.name}")