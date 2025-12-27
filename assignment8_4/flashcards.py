import random

def import_deck(filename):
    deck = []
    try:
        source = open(filename, "r")
        for line in source:
            line = line.rstrip()
            parts = line.split("|")
            if len(parts) == 2:
                prompt, response = parts[0], parts[1]
                deck.append({'prompt': prompt.strip(), 'response': response.strip(), 'revisions': 0})
            else:
                print(f"WARNING: Could not read line: {line}")
        source.close()

    except OSError:
        print(f"ERROR: The file {filename} could not be read.")
        return []
    return deck

def print_card(card):
    print()
    print(card['prompt'])
    print()
    input("Press enter to flip...\n")
    print(card['response'])
    print()

def main():
    filename = input("Which deck would you like to open?\n")
    deck = import_deck(filename)
    if len(deck) == 0:
        print("The deck is empty. Quitting...")
        return
    random.seed(int(input("Enter a seed:\n")))
    max_revisions = int(input("How many times would you like to revise one card?\n"))
    while len(deck) != 0:
        card = random.choice(deck)
        print_card(card)
        remembered_remaining = max_revisions - card['revisions'] - 1
        user_input = ''
        while user_input not in ['q', 'a', 'r']:
            user_input = input(f"[q]uit, [a]gain (reset progress), [r]emembered ({remembered_remaining} times left):\n")
        if user_input == 'a':
            card['revisions'] = 0
        elif user_input == 'r':
            card['revisions'] += 1
            if card['revisions'] >= max_revisions:
                deck.remove(card)
        else:
            return
    print("Session complete!")
main()