def cal_fee(info, distance, car_type):
    base_fee = float(info[car_type])
    fee_km = float(info[3]) * distance
    minutes = float(distance) / 55.0 * 60
    fee_min = float(info[4]) * minutes
    return base_fee + fee_km + fee_min

def main():
    distance = float(input("How long is the route (km)?\n"))
    while distance <= 0:
        print("Enter a positive length!")
        distance = float(input("How long is the route (km)?\n"))

    passengers = int(input("How many passengers?\n"))
    while not 1 <= passengers <= 8:
        print("The number of the passengers must be between 1 and 8.")
        passengers = int(input("How many passengers?\n"))
    if 1 <= passengers <= 4:
        car_type = 1
    else:
        car_type = 2
    print()
    name = input("Enter the filename. \n")

    try:
        source = open(name, "r")
        source.readline()
        lowest_fare = float("inf")
        cheapest_brand = ""

        for line in source:
            line = line.rstrip()
            info = line.split(",")
            try:
                if len(info) == 5:
                    fee = cal_fee(info, distance, car_type)
                    if fee <= lowest_fare:
                        lowest_fare = fee
                        cheapest_brand = info[0]
                elif len(info) > 0:
                    print("Invalid line:", line)

            except ValueError:
                print("Invalid line:", line)

        source.close()
        print()
        print(f"{cheapest_brand:s} has the cheapest fare and it is {lowest_fare:.2f} euros.")

    except OSError:
        print("Error while reading the file. Closing program.")

main()