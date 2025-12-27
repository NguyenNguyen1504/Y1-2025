# Y1 AUTUMN 2025
# Basic Course in Programming Y1
# Author: Priska Viljakainen
# Program to be run in exercise 9.1

from apartment import Apartment

def main():
    address_first = input("Enter the address of the first apartment:\n")
    rent_first = float(input("Enter the rent of the apartment:\n"))
    square_meters_first = float(input("Enter the square metres of the apartment:\n"))
    apartment1 = Apartment(address_first, rent_first, square_meters_first)

    address_second = input("Enter the address of the second apartment:\n")
    rent_second = float(input("Enter the rent of the apartment:\n"))
    square_meters_second = float(input("Enter the square metres of the apartment:\n"))
    apartment2 = Apartment(address_second, rent_second, square_meters_second)

    print("Updating rents.")
    price_change = float(input(f"Enter the new rent for the aparment in {apartment1.get_address()}?\n"))
    apartment1.change_rent(price_change)
    price_change = float(input(f"Enter the new rent for the aparment in {apartment2.get_address()}?\n"))
    apartment2.change_rent(price_change)

    print("Let's add the water charges to the total housing costs.")
    water = float(input(f"Enter the water charge for the aparment in {apartment1.get_address()}?\n"))
    total_costs1 = apartment1.calculate_total_housing_costs(water)
    print(f"Total housing costs for the apartment are now {total_costs1} euros.")
    water = float(input(f"Enter the water charge for the aparment in {apartment2.get_address()}?\n"))
    total_costs2 = apartment2.calculate_total_housing_costs(water)
    print(f"Total housing costs for the apartment are now {total_costs2} euros.")

    print("Printing the information of the apartments.")
    print()
    print(apartment1)
    print()
    print(apartment2)

main()