def main():
    CM_PER_KM = 100000
    scale = int(input("What is the map scale 1:n?\n"))
    while scale <= 0:
        scale = int(input("What is the map scale 1:n?\n"))

    measurement = float(input("What was the measurement in centimeters (negative numbers to quit)?\n"))

    while measurement >= 0:

        scaled_distance_cm = scale * measurement
        scaled_distance_km = scaled_distance_cm / CM_PER_KM

        print("The scaled distance in kilometers is", scaled_distance_km)

        measurement = float(input("What was the measurement in centimeters (negative numbers to quit)?\n"))

    print("Quitting...")

main()