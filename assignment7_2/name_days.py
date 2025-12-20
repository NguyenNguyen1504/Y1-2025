def main():
    file_name = input("Enter the name of the file to be read: \n")
    try:
        source = open(file_name, "r")
        name = input("What is the name we are looking for? \n")
        found = False
        for line in source:
            parts = line.rstrip().split(",")
            if name in parts:
                print(f"{name}'s name day is on {parts[0]}")
                found = True
        source.close()
        if not found:
            print(f"Could not find {name}'s name day.")

    except OSError:
        print(f"Error in reading the file {file_name}. Program ends.")

main()
