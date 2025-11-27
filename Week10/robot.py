from Week10.inhabitant import Inhabitant


class Robot(Inhabitant):

    def __init__(self, name, age, energy):
        self.name = name
        self.age = age
        self.energy = energy

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f"name = {self.name}, age = {self.age}, energy = {self.energy}"

    def __str__(self):
        return f"I am {self.name}, {self.age} years old and have {self.energy} energy."

    def grow(self):
        self.age += 1

    def eat(self, amount):
        if self.energy + amount >= self.MAX_ENERGY:
            self.energy += amount

    def distance(self, distance):
        if self.energy >= distance:
            self.energy -= distance
