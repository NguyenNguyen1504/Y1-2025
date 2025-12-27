# Y1 AUTUMN 2025
# Basic Course in Programming Y1
# Author: Priska Viljakainen
# Example solution for Exercise 9.1

# The class represents an apartment

class Apartment:
    MAX_INCREASE = 1.05        # %
    MAX_DECREASE = 0.90        # %

    # The method initializes a new apartment object
    # The address, rent and square meters of the apartment
    # are given as parameters
    def __init__(self, address, rent, square_meters):
        self.__address = address
        self.__rent = rent
        self.__square_meters = square_meters
        self.__total_housing_costs = rent

    # The method returns the address of the apartment
    def get_address(self):
        return self.__address
    
    # The method returns the rent of the apartment
    def get_rent(self):
        return self.__rent

    # The method returns the square meters of the apartment
    def get_square_meters(self):
        return self.__square_meters

    # The method returns the price per square meter
    def get_price_per_square_meter(self):
        return self.__rent / self.__square_meters
    
    # The method increases or decreases the rent
    def change_rent(self, new_rent):
        max_rent = self.MAX_INCREASE * self.__rent
        min_rent = self.MAX_DECREASE * self.__rent
        if new_rent > max_rent:
            self.__rent = max_rent
        elif new_rent < min_rent:
            self.__rent = min_rent
        else:
            self.__rent = new_rent


    # The method calculates the total housing costs
    def calculate_total_housing_costs(self, water_charge):
        self.__total_housing_costs = water_charge + self.__rent
        return self.__total_housing_costs

    # The method returns a string representation of the information
    # of the apartment
    def __str__(self):
        info = f"Address: {self.__address}\n"
        info += f"Rent: {self.__rent:.2f} euros.\n"
        info += f"Price per square meter: {self.get_price_per_square_meter():.2f} euros.\n"
        info += f"Total housing costs: {self.__total_housing_costs:.2f} euros.\n"
        return info  



