def main():
    INITIAL_FEE = 1.5
    FEE_PER_MINUTE = 0.22
    minutes = 0
    total = 0

    print("This program will record your electric scooter trips.")
    distance = int(input("Enter the length of the first trip (min). End with a negative value.\n"))

    while distance >= 0:
        total += INITIAL_FEE
        minutes += distance
        distance = int(input("Enter the length of the next trip (min). End with a negative value.\n"))

    total += minutes * FEE_PER_MINUTE
    if minutes >= 0:
        print("You spent a total of", minutes, "minutes and", total, "euros on your electric scooter trips.")
    else:
        print("You did not enter any trips.")


main()