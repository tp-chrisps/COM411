import matplotlib.pyplot as plt

def display_line(x, y):
    plt.plot(x, y)
    plt.show()

def small():
    x = [3, 4, 4, 3, 3]
    y = [3, 3, 4, 4, 3]
    plt.plot(x, y, 'ro:')

def medium():
    x = [2, 5, 5, 2, 2]
    y = [2, 2, 5, 5, 2]
    plt.plot(x, y, 'gs--')

def large():
    x = [1, 6, 6, 1, 1]
    y = [1, 1, 6, 6, 1]
    plt.plot(x, y, 'bx-')

def coordinate():
    x = int(input("X coordinate: "))
    y = int(input("Y coordinate: "))
    return x, y

def path():
    print("Retrieving path...")
    x_values = []
    y_values = []
    for i in range(4):
        x, y = coordinate()
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values

def run_task1():
    x_values = [1,2,3,4,5]
    y_values = [1,4,9,16,25]
    display_line(x_values, y_values)

def run_task2():
    small()
    medium()
    large()
    plt.show()

def run_task3():
    values = path()
    plt.plot(values[0], values[1], 'ro--')
    plt.show()

if __name__ == "__main__":
    run_task3()
