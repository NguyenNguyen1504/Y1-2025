class Square:
    EMPTY = " "

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__disc = Square.EMPTY

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_disc(self):
        return self.__disc

    def set_disc(self, new_disc):
        self.__disc = new_disc

    def __str__(self):  # Not needed othewise, but may be useful for debugging i.e. print(square)
        return f"SQUARE: ({self.__x}, {self.__y}) {self.__disc}"