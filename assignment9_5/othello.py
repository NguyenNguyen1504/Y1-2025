from player import Player
from square import Square


class Othello:
    SIZE = 4  # Must be 4, 6, 8 or 10. Change this to 8 to have a real Othello game with 8x8 board.
    DIRECTIONS = [
        [-1, -1], [0, -1], [1, -1],
        [-1, 0], [1, 0],
        [-1, 1], [0, 1], [1, 1]
    ]

    def __init__(self, player1, player2):
        self.__player1 = player1
        self.__player2 = player2
        self.__board = []
        for i in range(Othello.SIZE):
            row = []
            for j in range(Othello.SIZE):
                row.append(Square(j, i))
            self.__board.append(row)
        middle = Othello.SIZE // 2
        self.__board[middle - 1][middle - 1].set_disc(player2.get_checker())
        self.__board[middle - 1][middle].set_disc(player1.get_checker())
        self.__board[middle][middle - 1].set_disc(player1.get_checker())
        self.__board[middle][middle].set_disc(player2.get_checker())

    # Checks whether coordinates (x, y) are on the board
    def is_on_board(self, x, y):
        return 0 <= x < Othello.SIZE and 0 <= y < Othello.SIZE

    # Returns Square object located in column x, row y
    def get_square(self, x, y):
        if self.is_on_board(x, y):
            return self.__board[y][x]
        else:
            return None

    # Return the Square object that is the neighbor of the given square in the specified direction.
    def get_neighbor(self, square, direction):
        new_x = square.get_x() + direction[0]
        new_y = square.get_y() + direction[1]
        if self.is_on_board(new_x, new_y):
            return self.get_square(new_x, new_y)
        else:
            return None

    # Checks whether there are at least one possible move for player
    def moves_available(self, player):
        for row in self.__board:
            for square in row:
                if square.get_disc() == Square.EMPTY and self.find_flips(square, player) != []:
                    return True
        return False

    # Finds the squares where the disc has to be flipped if player inserts their disc in square.
    # Returns the list of those Square objects or an empty list, if is is not possible for player to
    # insert disc in square.
    def find_flips(self, square, player):
        if square.get_disc() != Square.EMPTY:
            return []
        to_flipped = []
        starting_square = square
        for direction in Othello.DIRECTIONS:
            new_square = self.get_neighbor(starting_square, direction)
            dir_list = []
            while new_square != None and new_square.get_disc() != Square.EMPTY and new_square.get_disc() != player.get_checker():
                dir_list.append(new_square)
                new_square = self.get_neighbor(new_square, direction)
            if dir_list != [] and new_square != None and new_square.get_disc() == player.get_checker():
                to_flipped += dir_list
        return to_flipped

    def move(self, x, y, player):
        square = self.get_square(x, y)
        flips = self.find_flips(square, player)
        if flips != []:
            square.set_disc(player.get_checker())
            for square in flips:
                square.set_disc(player.get_checker())
            return True
        else:
            return False

    def is_ended(self):
        if self.moves_available(self.__player1) or self.moves_available(self.__player2):
            return False
        else:
            return True

    def count_points(self, player):
        count = 0
        for row in self.__board:
            for square in row:
                if square.get_disc() == player.get_checker():
                    count += 1
        return count

    # Decide which player won and returns that player. If it is tie, the method return None.
    # This method works correctly only if it is called after the game has ended.
    def decide_winner(self):
        player1_points = self.count_points(self.__player1)
        player2_points = self.count_points(self.__player2)
        if player1_points > player2_points:
            return self.__player1
        elif player1_points < player2_points:
            return self.__player2
        else:
            return None

    def __str__(self):
        string = "    0"
        for i in range(1, Othello.SIZE):
            string += f"{i:4d}"
        string += "  \n"
        string += "  ┏" + (Othello.SIZE - 1) * "━━━┯" + "━━━┓\n"

        for y in range(Othello.SIZE):
            string += f"{y} ┃"
            for x in range(Othello.SIZE):
                string += f" {self.__board[y][x].get_disc()} "
                if x < Othello.SIZE - 1:
                    string += "│"
            string += "┃\n"
            if y < Othello.SIZE - 1:
                string += "  ┠" + (Othello.SIZE - 1) * "───┼" + "───┨\n"

        string += "  ┗" + (Othello.SIZE - 1) * "━━━┷" + "━━━┛"
        string += "\n"
        string += "\n"
        string += f"   {self.__player1.get_name():^15}{self.__player2.get_name():^15} \n"
        string += "   ━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━\n"
        string += f"   {self.count_points(self.__player1):^15}│{self.count_points(self.__player2):^15}\n"

        return string