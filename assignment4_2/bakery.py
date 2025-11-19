import math

def cookies(servings):
    SUGAR_COOKIES = 4.4
    BUTTER = 9
    FLOUR_COOKIES = 11
    CHOCOLATE_CHIPS = 3
    needed_sugar = SUGAR_COOKIES * servings
    needed_butter =  BUTTER * servings
    needed_flour =  FLOUR_COOKIES * servings
    needed_chocolate =  CHOCOLATE_CHIPS * servings
    print()
    print("For the cookies you need:")
    print(f"{needed_sugar:.2f} g of sugar.")
    print(f"{needed_butter} g of butter.")
    print(f"{needed_flour} g of flour.")
    print(f"{needed_chocolate} g of chocolate chips.")

def cake(servings):
    EGGS = 4
    FLOUR_CAKE = 100
    SUGAR_CAKE = 148
    MILK = 3
    SERVING_SIZE = 12
    print("One cake serves 12 people.")
    CAKE = math.ceil(servings / SERVING_SIZE)
    if CAKE == 1:
        print(f"You only need to make {CAKE} cake!")
    else:
        print(f"You need to make {CAKE} cakes!")

    needed_sugar = SUGAR_CAKE * CAKE
    needed_eggs = EGGS * CAKE
    needed_flour = FLOUR_CAKE * CAKE
    needed_milk = MILK * CAKE
    print()
    print("Here are your ingredients:")
    print(f"{needed_sugar} g of sugar.")
    print(f"{needed_eggs} eggs.")
    print(f"{needed_flour} g of flour.")
    print(f"{needed_milk} dl of milk.")

def main():
    choice = input("What do you want to make (0=cookies, 1=cake)? \n")
    servings = int(input("For how many people are you baking for? \n"))
    if choice == "0":
        cookies(servings)
    else:
        cake(servings)

main()