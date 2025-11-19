def main():
    PARS = [1, 2, 3, 4, 2, 3, 5, 3, 2]
    ROUND = [""] * len(PARS)

    print("The pars for the holes are:")
    for i in range(len(PARS)):
        print(f"HOLE {i+1}: {PARS[i]}")

    for i in range(len(PARS)):
        ask = int(input(f"Enter the number of strokes for the hole {i+1}: \n"))
        if ask == PARS[i]:
            ROUND[i] = f"On hole {i+1} you scored a par!"
        elif ask > PARS[i]:
            ROUND[i] = f"On hole {i+1} you scored above par!"
        else:
            ROUND[i] = f"On hole {i+1} you scored below par!"

    print("Here is how your round went:")
    for turn in ROUND:
        print(turn)

main()