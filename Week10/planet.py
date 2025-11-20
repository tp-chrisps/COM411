class Planet:
    def __init__(self, name):
        self.inhabitants = {
            "humans": [],
            "robots": []
        }
        self.name = name

    def add_human(self, human):
        self.inhabitants["humans"].append(human.name)

    def add_robot(self, robot):
        self.inhabitants["robots"].append(robot.name)

    def remove_human(self, human):
        self.inhabitants["humans"].remove(human.name)

    def remove_robot(self, robot):
        self.inhabitants["robots"].remove(robot.name)

    def __repr__(self):
        return f'name={self.name}, humans={self.inhabitants["humans"]}, robots={self.inhabitants["robots"]}'

    def __str__(self):
        return f'Planets name is {self.name}, humans is {self.inhabitants["humans"]}, robots is {self.inhabitants["robots"]}'
