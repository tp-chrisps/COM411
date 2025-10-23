def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return likelihoods

def steps():
    likelihoods = [("Step 1", 50), ("Step 2", 38), ("Step 3", 27), ("Step 4", 99), ("Step 5", 4)]
    return likelihoods

def run_task1():
    tuple = likelihood()
    print(f"Minimun likelihood of falling: {min(tuple)}% ")

def run_task2():
    tuple = likelihood()
    return max(tuple)

def run_task3():
    list = steps()
    good_steps = []
    bad_steps = []
    for step in list:
        if step[1] < 50:
            good_steps.append(step)
        else:
            bad_steps.append(step)
    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")


run_task1()
print(f"Maximum likelihood of falling: {run_task2()}%")
run_task3()