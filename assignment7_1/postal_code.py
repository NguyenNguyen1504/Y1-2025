def main():
    HELSINKI_SMALLEST = 2
    HELSINKI_GREATEST = 990
    ESPOO_SMALLEST = 2100
    ESPOO_GREATEST = 2980

    name = input("Enter a filename: \n")
    try:
        helsinki = 0
        espoo = 0
        other = 0
        source = open(name, "r")

        for line in source:
            postal_code = int(line)
            if HELSINKI_SMALLEST <= postal_code <= HELSINKI_GREATEST:
                helsinki += 1
            elif ESPOO_SMALLEST <= postal_code <= ESPOO_GREATEST:
                espoo += 1
            else:
                other += 1
        source.close()
        all_places = helsinki + espoo + other
        if all_places == 0:
            print("The file didn't contain any data.")
        else:
            h_per = helsinki / all_places * 100.0
            e_per = espoo / all_places * 100.0
            o_per = other / all_places * 100.0
            print("Of all the postal codes observed: ")
            print(f"{helsinki} were in Helsinki, which is {h_per:.1f} %.")
            print(f"{espoo} were in Espoo, which is {e_per:.1f} %.")
            print(f"{other} were elsewhere, which is {o_per:.1f} %.")

    except ValueError:
        print(f"Incorrect line in file {name}. Closing program.")

    except OSError:
        print(f"Error in reading file {name}. Closing program.")

main()