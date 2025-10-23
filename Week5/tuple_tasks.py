def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return likelihoods

def run_task1():
    tuple = likelihood()
    print(f"Minimun likelihood of falling: {min(tuple)}% ")

def run_task2():
    tuple = likelihood()
    return max(tuple)

run_task1()
print(f"Maximum likelihood of falling: {run_task2()}%")