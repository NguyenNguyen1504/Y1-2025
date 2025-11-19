def main():
    LIMIT = 6.75                        # meters
    FIELD_GOAL_NORMAL = 2
    THREE_POINTER = 3

    number_of_goals = int(input("How many field goals did you make?\n"))
    field_goals = [0.0] * number_of_goals
    for i in range(number_of_goals):
        one_goal = float(input(f"How far from the basket did you throw the field goal {i+1} (m)?\n"))
        field_goals[i] = one_goal
    print("Field goals:")

    total = 0

    for goal in field_goals:
        if goal >= LIMIT:
            total += THREE_POINTER
            print("3 points")
        else:
            total += FIELD_GOAL_NORMAL
            print("2 points")

    print(f"You got {total} points in total!")


    # Implement your own code here that goes through the list of
    # distances and prints the points from each field goal

    # Write then your own code here that prints the total points

main()