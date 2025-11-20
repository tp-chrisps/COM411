from Week10.planet import Planet
from human import Human
from robot import Robot
if __name__ == '__main__':
    human = Human("Human", 0, 0)
    human.display()
    robot = Robot("Robot", 0, 0)
    robot.display()
    human2 = Human("Human2", 0, 0)
    planet = Planet("Planet")
    planet.add_human(human)
    planet.add_human(human2)
    planet.add_robot(robot)
    print(planet)
    planet.remove_human(human)
    print(repr(planet))
