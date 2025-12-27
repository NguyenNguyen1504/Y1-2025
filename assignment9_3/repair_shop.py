# Y1 AUTUMN 2022
# Basic Course in Programming Y1
# Author: Roosa Rauhala
# A simple testing class given in Exercise 9.3

import product
import random


# Prints some information about the product
# parameters: product0 - the product in question (Product)
# This function is here for testing purposes, in case the student's __str__ method is not functional
# otherwise, it wouldn't be necessary
def print_info(product0):
    print(product0.get_name())
    print("Value:", product0.get_value())
    print("Condition:", product0.get_condition())
    print("Hours used after the latest repair:", product0.get_hours_used())
    print("Total hours used:", product0.get_total_hours_used())


def main():
    product1 = product.Product("Charger", 10.5, 5)
    print("Initial description of the product using the __str__ method:")
    print(product1)
    product1.fix_product()
    print("After fixing it:")
    print_info(product1)
    product1.use(5)
    print("After using it for less than 10 hours:")
    print_info(product1)
    product1.use(6)
    print("After using it for more than 10 hours:")
    print_info(product1)
    product1.break_item()
    print("After breaking the item:")
    print_info(product1)
    product1.use(11)
    print("After using it for 11 hours:")
    print_info(product1)
    print("After attempting to quickly fix it:")
    # setting the seed
    random.seed(7)
    if product1.quick_fix():  # should return Failure
        print("Success!")
        print_info(product1)
        print("However, the attempt should have been unsuccessful. Check your code for errors.")
    else:
        print("Failure")
        print_info(product1)
        print("After attempting to quickly fix it:")
        if product1.quick_fix():  # should return Success
            print("Success!")
            print_info(product1)
        else:
            print("Failure")
            print_info(product1)
            print("However, the attempt should have been successful. Check your code for errors.")
    print("Final description of the product using the __str__ method:")
    print(product1)
    print("Creating another product")
    product2 = product.Product("Toaster", 30, 8)
    print("Attempting to quickly fix it")
    product2.quick_fix()  # should fail
    print("Using it for 20 hours")
    product2.use(20)
    print("Final description of the product using the __str__ method after performing all the actions mentioned above:")
    print(product2)


main()
