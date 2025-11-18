def count_steps(day, stride_length):
    journey_count = 1
    distance_in_meters = int(input(f"Distance of the journey {journey_count} in meters: \n"))
    total_distance = 0
    while distance_in_meters >= 0:
        total_distance += distance_in_meters
        journey_count += 1
        distance_in_meters = int(input(f"Distance of the journey {journey_count} in meters: \n"))

    total_steps = int(total_distance / stride_length)
    print(f"You walked {total_steps} steps on the day {day}!")
    return total_steps

def main():
    height_in_meters = int(input("Enter your height in cm: \n")) / 100
    stride_length = height_in_meters * 0.413
    days = int(input("How many days do you want to record? \n"))
    completed_days = 0

    for i in range(days):
        step_goal = int(input(f"What is your step goal for the day {i+1}? \n"))
        print(f"Enter the journeys you walked on the day {i+1}. Enter a negative number when you have entered all the journeys. \n")

        total_steps = count_steps(i+1, stride_length)

        if total_steps > step_goal:
            completed_days += 1


    print(f"You reached your step goal on {completed_days} days(s)!")

main()
