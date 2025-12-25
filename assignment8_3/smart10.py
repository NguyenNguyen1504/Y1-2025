import random

def main():
    filename = input("Enter a filename:\n")
    seed = int(input("Enter a seed: \n"))
    random.seed(seed)
    questions = {}
    try:
        file = open(filename, "r")
        for line in file:
            line = line.rstrip()
            parts = line.split(",")
            if len(parts) == 12:
                key, values = parts[0], parts[1:]
                questions[key] = values

        file.close()
        total_points = 0
        for i in range(3):
            chosen = random.choice(list(questions.keys()))

            options = questions[chosen]
            options_list, answers_list = options[:-1], options[-1]
            answers_list = answers_list.split()
            for order in range(len(answers_list)):
                answers_list[order] = int(answers_list[order])

            print()
            print(chosen)
            index = 1
            for option in options_list:
                print(f"{index}. {option}")
                index += 1

            points = 0
            guessed = []
            user_choice = int(input("Which answers apply to the statement? Enter the answer number, or 0 to continue to the next question.\n"))

            while user_choice != 0:
                if user_choice in guessed:
                    print("You have already guessed that!")
                else:
                    guessed.append(user_choice)
                    if user_choice in answers_list:
                        print("Correct!")
                        points += 1
                    else:
                        print("Incorrect!\nYou lose all the points you gathered this round!")
                        points = 0
                        break
                user_choice = int(input("Which answers apply to the statement? Enter the answer number, or 0 to continue to the next question.\n"))
            print(f"You claimed {points} points this round.")
            total_points += points
            del questions[chosen]
        print(f"You got {total_points} points in total!")

    except OSError:
        print(f"Error in reading the file {filename}. Closing program.")

main()