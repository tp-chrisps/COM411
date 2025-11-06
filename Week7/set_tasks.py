def observed():
    observations = {"Car",
                    "Sky Scraper",
                    "Sky Scraper",
                    "Bike",
                    "House",
                    "House"}
    return observations

def observed_items():
    observations = set()
    for i in range(5):
        observ = input("Please enter an observation:\n")
        observations.add(observ)
    return observations

def remove_observation(observation):
    remove = input("Please enter an observation to remove:\n")
    observation.remove(remove)
    return observation

def run_task3():
    observations = observed_items()
    choice = "y"
    while choice == "y":
        choice = input("Do you wish to remove an observation?(y/n)\n")
        if choice == "y":
            observations = remove_observation(observations)
    print(observations)

if __name__ == "__main__":
    run_task3()

