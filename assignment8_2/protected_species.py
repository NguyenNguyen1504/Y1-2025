def read_file(filename):
    species = {}
    try:
        file = open(filename, "r")
        for line in file:
            line = line.rstrip()
            parts = line.split(",")
            name = parts[0]
            value = parts[1]
            try:
                value = int(value)
                species[name] = value
            except ValueError:
                print(f"WARNING: Could not read line: {line}")

    except OSError:
        print(f"ERROR: Could not read file: {filename}")
    return species

def get_total_and_max(species_values, found_species):
    total = 0
    chosen = ""
    highest = -1
    for species in found_species:
        if species in species_values:
            points = species_values[species] * found_species[species]
            total += points
            if highest < points:
                highest = points
                chosen = species
        else:
            print(f"INFO: {species} does not have a value.")
    return total,chosen,highest

def main():

    species_values = read_file(input("File of protected species values:\n"))
    found_species = read_file(input("File of found species and counts:\n"))
    if len(species_values) == 0 or len(found_species) == 0:
        print("Quitting...")
        return

    total, max_species, max_species_total = get_total_and_max(species_values, found_species)
    if max_species_total == -1:
        print("Could not find values for any species...")
    else:
        print(f"The total is {total} euros with the highest value of {max_species_total} euros by {max_species}.")

main()


