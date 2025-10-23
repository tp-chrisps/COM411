from matplotlib.lines import drawStyles


def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps

def movements():
    path = []
    return path

def menu():
    print("Please enter a direction:")
    direction = input("0: Move forward \n1: Move backward \n2: Turn left \n3: Turn right")
    steps = directions()
    steps.append(direction)
    for i in range(len(steps)):
        print(f"{i}: {steps[i]}")

def menu_and_input():
    path = movements()
    for i in range(5):
        print("Please enter a direction:")
        direction = input("0: Move forward \n1: Move backward \n2: Turn left \n3: Turn right")
        path.append(direction)
    return path


def run_task1():
    if __name__ == "__main__":
        print(directions())

def run_task2():
    path = movements()
    for i in range(0,path.__len__(),2):
        print(f"{path[i]} for {path[i+1]} steps")

def run_task3():
    menu()

def run_task4():
    route = menu_and_input()
    print("Escape route: ", route)

run_task4()