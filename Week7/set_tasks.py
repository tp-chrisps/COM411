def observed():
    observations = {"Car",
                    "Sky Scraper",
                    "Sky Scraper",
                    "Bike",
                    "House",
                    "House"}
    return observations

def observed_items():
    observations = {}
    for i in range(7):
        observ = input("Please enter an observation:\n")
        if observ not in observations:
            observations[observ] = 1
        else:
            observations[observ] += 1
    for item in observations:
        print(f"{item}: observed {observations[item]}times ")
def run_task2():
    observed_items()

if __name__ == "__main__":
    run_task2()

