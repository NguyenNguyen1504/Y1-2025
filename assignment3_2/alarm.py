def main():
    hours_1 = 8
    minutes_1 = 0
    hours_2 = 8
    minutes_2 = 0
    print(f"It is {hours_1:02d}:{minutes_1:02d}!")
    print("Choose an action:\n")
    print("0. Snooze.\n")
    print("1. Wake up.\n")
    choice = int(input())
    while choice == 0:
        minute = int(input("For how many minutes do you want to snooze? \n"))
        minutes_2 += minute
        hours_2 += minutes_2 // 60
        minutes_2 %= 60

        print(f"It is {hours_2:02d}:{minutes_2:02d}!")
        print("Choose an action:\n")
        print("0. Snooze.\n")
        print("1. Wake up.\n")
        choice = int(input())
    print("Good morning!")

main()