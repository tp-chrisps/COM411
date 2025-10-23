def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return likelihoods

def run_task1():
    tuple = likelihood()
    print(f"Minimun likelihood of falling: {min(tuple)}% ")

run_task1()