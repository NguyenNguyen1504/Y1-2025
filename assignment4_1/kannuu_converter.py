def kannus_to_liters():
    k = float(input("How many kannus? \n"))
    l = k * 2.6172
    print(f"{k} kannus is {l:.2f} liters")

def liters_to_kannus():
    l = float(input("How many liters? \n"))
    k = l / 2.6172
    print(f"{l} liters is {k:.2f} kannus")


def main():
    print("Welcome to the kannu converter!")
    choice = -1
    while choice != 3:
        print("1) kannus to liters")
        print("2) liters to kannus")
        print("3) quit")
        choice = int(input())
        print()
        if choice == 1:
            kannus_to_liters()
        elif choice == 2:
            liters_to_kannus()
        print()


main()

