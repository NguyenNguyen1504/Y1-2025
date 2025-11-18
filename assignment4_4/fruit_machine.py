import random


def ask_and_set_seed(input_text):
    user_seed = int(input(input_text))
    random.seed(user_seed)


def get_random_fruits():
    fruits = ['🍇', '🍉', '🍊', '🍋', '🥭', '🍎', '🍐', '🍑', '🍒', '🥝']
    fruit1 = random.choice(fruits)
    fruit2 = random.choice(fruits)
    fruit3 = random.choice(fruits)
    return fruit1, fruit2, fruit3


def print_slots(fruit1, fruit2, fruit3):
    slots = f"""
╔════════════╗
║┌──┐┌──┐┌──┐║
║│{fruit1}││{fruit2}││{fruit3}│║
║└──┘└──┘└──┘║
╚════════════╝\n"""
    print(slots)

def determine_reward(coins, fruit1, fruit2, fruit3):
    if fruit1 == fruit2:
        if fruit3 == fruit1:
            print("Jackpot! You get 10 coins.")
            return coins + 10 - 1
        else:
            print("Double! You get 3 coins.")
            return coins + 3 - 1
    else:
        if fruit3 == fruit1 or fruit3 == fruit2:
            print("Double! You get 3 coins.")
            return coins + 3 - 1
        else:
            print("You did not get any coins.")
            return coins - 1

def ask_for_coins(minimum_coins, maximum_coins):
    amount = int(input("How many coins would you like to insert? \n"))
    while amount < minimum_coins or amount > maximum_coins:
        amount = int(input("How many coins would you like to insert? \n"))
    return amount

def ask_to_play(coins):
    choice = int(input(f"You have {coins} coins. Would you like to continue (yes=1, no=0)? \n"))
    while choice != 1 and choice != 0:
        choice = int(input("Would you like to continue (yes=1, no=0)? \n"))
    if choice == 1:
        return True
    else:
        return False

def goodbye_print(coins, initial_coins):
    difference = initial_coins - coins
    if difference > 0:
        print(f"You lost {difference} coin(s).")
    elif difference < 0:
        print(f"You won {-difference} coin(s).")
    else:
        print("You did not win anything...")

def main():
    user_seed = int(input("What is your lucky number?\n"))
    random.seed(user_seed)
    current_coins = ask_for_coins(1, 100)
    initial_coins = current_coins
    play_again = True

    while play_again and current_coins > 0:
        random_fruit1, random_fruit2, random_fruit3 = get_random_fruits()
        print_slots(random_fruit1, random_fruit2, random_fruit3)
        current_coins = determine_reward(current_coins, random_fruit1, random_fruit2, random_fruit3)
        if current_coins > 0:
            play_again = ask_to_play(current_coins)

    goodbye_print(current_coins, initial_coins)


main()