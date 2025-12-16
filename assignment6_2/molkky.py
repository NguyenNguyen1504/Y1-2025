def count_points(points):
    if len(points) == 1:
        return int(points[0])
    else:
        return len(points)


def main():
    print("Enter all players. Stop with an empty line.")
    ask_name = input("Enter the name of the player:\n")
    players = {}
    while ask_name != "":
        if ask_name in players:
            print(f"You've already added {ask_name}.")
        else:
            players[ask_name] = 0
        ask_name = input("Enter the name of the player:\n")

    winner = ""
    while winner == "":
        for name in players:
            if winner == "":
                print(f"{name}'s turn!")
                skittle_input = input(
                    "Enter all the skittles that were knocked over, separate the numbers by commas:\n")
                skittles = skittle_input.split(",")
                players[name] += count_points(skittles)
                if players[name] == 50:
                    winner = name
                elif players[name] > 50:
                    players[name] = 25
                print()
                print("Current situation:")
                for player in players:
                    print(f"{player}: {players[player]}")
                print()
    print(f"The winner is {winner}!")

main()
