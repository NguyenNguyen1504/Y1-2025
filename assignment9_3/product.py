import random

class Product:
    FIX_VALUE = 20.0
    FIX_CONDITION = 2
    QUICK_FIX_VALUE = 50.0
    QUICK_FIX_CONDITION = 4
    TOP_CONDITION = 10

    def __init__(self, name, value, condition):
        self.__name = name
        if value < 0:
            self.__value = 0.0
        else:
            self.__value = value
        if 0 <= condition <= Product.TOP_CONDITION:
            self.__condition = condition
        else:
            self.__condition = 0
        self.__fixed = False
        self.__hours_used = 0
        self.__total_hours_used = 0

    def get_name(self):
        return self.__name

    def get_value(self):
        return self.__value

    def get_condition(self):
        return self.__condition

    def get_fixed(self):
        return self.__fixed

    def get_hours_used(self):
        return self.__hours_used

    def get_total_hours_used(self):
        return self.__total_hours_used

    def change_value(self, percent, increase):
        change = self.__value * (percent / 100.0)
        if increase:
            self.__value += change
        else:
            if self.__value - change < 0.0:
                self.__value = 0.0
            else:
                self.__value -= change

    def change_condition(self, amount, increase):
        if increase:
            if self.__condition + amount > Product.TOP_CONDITION:
                self.__condition = Product.TOP_CONDITION
            else:
                self.__condition += amount
        else:
            if self.__condition - amount < 0:
                self.__condition = 0
            else:
                self.__condition -= amount

    def fix_product(self):
        if not self.__fixed:
            self.change_value(Product.FIX_VALUE, True)
            self.change_condition(Product.FIX_CONDITION, True)
            self.__fixed = True
            self.__hours_used = 0

    def quick_fix(self):
        if not self.__fixed:
            rand = random.randint(0, 1)
            if rand == 0:
                self.change_value(Product.QUICK_FIX_VALUE, True)
                self.change_condition(Product.QUICK_FIX_CONDITION, True)
                self.__hours_used = 0
                self.__fixed = True
                return True
            else:
                self.change_value(Product.QUICK_FIX_VALUE, False)
                self.change_condition(Product.QUICK_FIX_CONDITION, False)
                return False
        else:
            return True

    def break_item(self):
        if self.__fixed:
            self.__fixed = False
            self.change_value(Product.FIX_VALUE, False)
            self.change_condition(Product.FIX_CONDITION + 1, False)

    def use(self, time):
        if time > 0:
            self.__hours_used += time
            self.__total_hours_used += time
            if self.__hours_used < 10:
                self.change_value(5.0, False)
            else:
                self.change_value(10.0, False)
                self.change_condition(1, False)

    def __str__(self):
        info = ""
        info += f"{self.__name:s}\n"
        info += f"Value: {self.__value:.2f} euros\n"
        info += f"Condition: {self.__condition:d}/10\n"
        if self.__fixed:
            helper = "The product has been repaired.\n"
        else:
            helper = "The product is currently broken.\n"
        info += helper
        info += "Hours used after the latest repair: {:d}\n".format(self.__hours_used)
        info += "Total hours used: {:d}".format(self.__total_hours_used)
        return info