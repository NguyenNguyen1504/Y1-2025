# Y1 AUTUMN 2022
# Basic Course in Programming Y1
# Author: Roosa Rauhala
# An interactive testing class given in Exercise 9.3

import product
import random


# Prints some information about the product
# parameters: product1 - the product in question (Product)
# This function is here for testing purposes, in case the student's __str__ method is not functional
# otherwise, it wouldn't be necessary
def print_info(product1):
    print(product1.get_name())
    print("Value:", product1.get_value())
    print("Condition:", product1.get_condition())
    print("Hours used after the latest repair:", product1.get_hours_used())
    print("Total hours used:", product1.get_total_hours_used())


# Asks the user to choose an action and performs it to the product. Repeats this process until the user enters the
# number 6 when asked for a new action.
# parameters: product1 - the product in question (Product)
def choose_action(product1):
    action = int(input('What would you like to do with the product? Write the corresponding number to choose an action.'
                       '\n1. Fix\n2. Quick fix\n3. Break\n4. Use\n5. Get description\n6. Stop\n'))
    while action != 6:
        if action == 1:
            if product1.get_fixed():
                print("The product has already been repaired.")
            else:
                product1.fix_product()
                print("A description of the product after repairing it")
                print_info(product1)
        elif action == 2:
            if product1.get_fixed():
                print("The product has already been repaired.")
            else:
                attempt = product1.quick_fix()
                if attempt:
                    print("A description of the product after successfully fixing it quickly")
                    print_info(product1)
                else:
                    print("A description of the product after unsuccessfully trying to fix it quickly")
                    print_info(product1)
        elif action == 3:
            product1.break_item()
            print("A description of the product after breaking it")
            print_info(product1)
        elif action == 4:
            hours = int(input("How long would you like to use it for?\n"))
            product1.use(hours)
            print("A description of the product after using it")
            print_info(product1)
        elif action == 5:
            print("The product's description")
            print(product1)
        action = int(input('What would you like to do with the product? Write the corresponding number to choose an action.'
                  '\n1. Fix\n2. Quick fix\n3. Break\n4. Use\n5. Get description\n6. Stop\n'))


def main():
    seed = input("Enter a seed for the random number generator:\n")
    random.seed(int(seed))
    name = input("Enter the name of the first product:\n")
    value = float(input("Enter its value:\n"))
    condition = int(input("Enter the product's condition out of ten:\n"))
    first_product = product.Product(name, value, condition)
    choose_action(first_product)
    name = input("Enter the name of the second product:\n")
    value = float(input("Enter its value:\n"))
    condition = int(input("Enter the product's condition out of ten:\n"))
    second_product = product.Product(name, value, condition)
    choose_action(second_product)
    print("Goodbye!")


main()
