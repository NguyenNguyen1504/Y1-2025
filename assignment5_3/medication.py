def moving_average(data, ws):
    length = len(data) - ws + 1
    avg = [0.0] * length
    if 0 < ws <= length:
        for i in range(length):
            count = i
            total = 0
            while count < ws + i:
                total += data[count]
                count += 1
            avg[i] = total / ws

    return avg

def all_in_range(data, min_value, max_value):
    flag = True
    for i in data:
        if i < min_value or i > max_value:
            flag = False
            break
    return flag


def main():
    minimum = float(input("What is the MINIMUM temperature the medication can tolerate?\n"))
    maximum = float(input("What is the MAXIMUM temperature the medication can tolerate?\n"))
    while minimum > maximum:
        minimum = float(input("What is the MINIMUM temperature the medication can tolerate?\n"))
        maximum = float(input("What is the MAXIMUM temperature the medication can tolerate?\n"))
    time = int(input("How many minutes to include in the average?\n"))
    while time <= 0:
        time = int(input("How many minutes to include in the average?\n"))
    measurement = int(input("How many measurements to input?\n"))
    while measurement < time:
        measurement = int(input("How many measurements to input?\n"))

    data = []
    print("Input measurements:")
    for i in range(measurement):
        new_measurement = float(input())
        data.append(new_measurement)
    log = moving_average(data, time)
    check = all_in_range(log, minimum, maximum)
    if check:
        print("The medication was stored properly!")
    else:
        print("The medication was not stored properly, check with the manufacturer...")

    print(f"Log: {log}")

main()