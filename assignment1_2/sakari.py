def main():
    number = int(input("Dress Sakari in a sweater (no=0, yes=1)?\n"))
    if number == 1:
        print('It tickles. You won the game!')
    elif number == 0:
        print('You lost the game!')
    else:
        print('Try again.')

main()