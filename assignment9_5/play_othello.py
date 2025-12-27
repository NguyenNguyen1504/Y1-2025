# Y1 AUTUMN 2025
# Basic Course in Programming Y1
# Author: Priska Viljakainen, Kerttu Pollari-Malmi
# Example solution for Exercise 9.5


from othello import Othello
from player import Player


def ask_coordinates():
    # Method asks for the column and row of the checker separated by a comma until the user input is valid.
    # Both values are given as an integer between 0 and Othello.SIZE - 1
    # Method returns the given integers.

    ok = False
    while not ok:
        try:
            coordinates = input("Enter the column and row of where you want to place a checker:\n").split(",")
            if (len(coordinates) == 2) and (0 <= int(coordinates[0]) < Othello.SIZE) and (
                    0 <= int(coordinates[1]) < Othello.SIZE):
                ok = True
            else:
                print("ERROR: Invalid coordinates.")
        except ValueError:
            print("ERROR: Invalid coordinates.")
    return int(coordinates[0]), int(coordinates[1])


def main():
    print("Welcome to play Othello!")
    name1 = input("Enter the name of the first player:\n")
    name2 = input("Enter the name of the second player:\n")
    player1 = Player(name1, "x")
    player2 = Player(name2, "o")
    game = Othello(player1, player2)
    player_in_turn = player1

    while not game.is_ended():
        print(game)
        if game.moves_available(player_in_turn):
            print(f"{player_in_turn.get_name()}'s ({player_in_turn.get_checker()}) turn!")
            coordinate1, coordinate2 = ask_coordinates()
            moved = game.move(coordinate1, coordinate2, player_in_turn)
            while not moved:
                print("You cannot put your checker there!")
                coordinate1, coordinate2 = ask_coordinates()
                moved = game.move(coordinate1, coordinate2, player_in_turn)
        else:
            print(f"{player_in_turn.get_name()} cannot move.")
        if player_in_turn == player1:
            player_in_turn = player2
        else:
            player_in_turn = player1
    print(game)
    print("Game ended.")
    winner = game.decide_winner()
    if winner == None:
        print("It is a tie!")
    else:
        print(f"The winner is {winner.get_name()}!")


main()