def main():
    user_input = int(input("How many species would you like to classify?\n"))
    critically_endangered = 0
    endangered = 0
    for n in range(1, user_input + 1):
        species = input(f"{n} | Species name: \n")

        population_count = int(input("Population count: \n"))
        while population_count < 0:
            population_count = int(input("Population count: \n"))

        population_change = float(input("Average population size change per year in percent: \n"))
        habitat_change = float(input("Average habitat size change per year in percent: \n"))
        classification = "LEAST CONCERN"
        if population_change >= 0 and habitat_change > -15:
            classification = "LEAST CONCERN"
        if population_change >= 0 and habitat_change <= -15:
            classification = "NEAR THREATENED"
        if population_change < 0 and population_count < 20000:
            classification = "VULNERABLE"
        if population_change < 0 and population_count < 10000 and habitat_change < -25:
            classification = "ENDANGERED"
        if population_change < 0 and population_count < 2500 and habitat_change < -50:
            classification = "CRITICALLY ENDANGERED"

        if classification == "CRITICALLY ENDANGERED":
            critically_endangered += 1
        if classification == "ENDANGERED":
            endangered += 1

        print(f"The species {species} is classified as {classification}. \n")
    print(f"There were {critically_endangered} critically endangered and {endangered} endangered species.")

main()