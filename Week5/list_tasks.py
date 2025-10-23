def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run_task2():
    path = movements()
    for i in range(0,path.__len__(),2):
        print(f"{path[i]} for {path[i+1]} steps")

run_task2()