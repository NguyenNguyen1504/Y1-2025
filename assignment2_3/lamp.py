def main():

    print("-- Lamp diagnostics --")

    user_input = int(input("Is the lamp switched on? (yes=1, no=0)\n"))

    if user_input == 0:
        print("Switch on the lamp.")
    else:
        user_input = int(input("Is the lamp plugged in? (yes=1, no=0)\n"))

        if user_input == 0:
            print("Plug the lamp into an outlet.")
        else:
            user_input = int(input("Do other electrical devices work in the room? (yes=1, no=0)\n"))

            if user_input == 0:
                print("Check the breaker.")
            else:
                print("The lamp should work, but I don't know why it doesn't...")

main()