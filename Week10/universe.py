from random import random
import numpy as np
import random
import matplotlib.pyplot as plt
from robot import Robot
from human import Human
from planet import Planet

class Universe:
    def __init__(self):
        self.planets = []

    def generate(self):
        planet = Planet(f"planet{len(self.planets)}")
        self.planets.append(planet)
        for i in range(random.randint(1,5)):
            human = Human(f"Human{i}", 0, 0)
            planet.add_human(human)
        for i in range(random.randint(1,5)):
            robot = Robot(f"Robot{i}", 0, 0)
            planet.add_robot(robot)

    def show_populations(self,selection):
        y = []
        x = []
        for planet in self.planets:
            x.append(planet.name)
            y.append(len(planet.inhabitants[selection]))
        plt.bar(x,y)
        plt.show()

    def __repr__(self):
        return f"planets = {self.planets},"