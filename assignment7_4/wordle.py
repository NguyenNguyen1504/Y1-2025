import random

INCORRECT = 0
MISPLACED = 1
CORRECT = 2

def print_the_word(guess, word):
    comparison = [INCORRECT, INCORRECT, INCORRECT, INCORRECT, INCORRECT]
    count = {}
    string = ""
    guess_string = ""

    for letter in word:
        if letter not in count:
            count[letter] = 0
        count[letter] += 1

    for i in range (5):
        if guess[i] == word[i]:
            comparison[i] = CORRECT
            count[guess[i]] -= 1

    for i in range(5):
        if comparison[i] != CORRECT and guess[i] in word and count[guess[i]] > 0:
            comparison[i] = MISPLACED
            count[guess[i]] -= 1

        if comparison[i] == CORRECT:
            guess_string += "+ "
        elif comparison[i] == MISPLACED:
            guess_string += "~ "
        else:
            guess_string += "- "

        string += (guess[i] + " ")

    print(string)
    print(guess_string)
    print()

def main():
    name = input("Enter the name of the file to be read:\n")
    seed_number = int(input("Enter a seed:\n"))
    random.seed(seed_number)

    try:
        source = open(name, "r")
        words = []
        for line in source:
            line = line.rstrip()
            parts = line.split()
            if len(parts) == 1:
                words.append(parts[0].upper())
        source.close()
        if len(words) != 0:
            ans = random.choice(words)
            print()
            print("- : NOT IN THE WORD")
            print("~ : MISPLACED")
            print("+ : CORRECT")
            print()

            turns = 6
            guess = ""
            while guess != ans and turns != 0:
                print(f"Turns left: {turns}")
                guess = input("Make a guess!\n").upper()
                while guess not in words:
                    guess = input("Not in the word list. Make a new guess!\n").upper()
                print_the_word(guess, ans)
                turns -= 1
                if guess == ans:
                    print("You won!")
            print(f"The word was {ans}.")
        else:
            print(f"There were no valid words in the file {name}. Program ends.")


    except OSError:
        print(f"Error in reading the file {name}. Program ends.")

main()

