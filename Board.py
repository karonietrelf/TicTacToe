class Board:
    """Class to represent a Board.

        Methods:
            create_empty_board: Used to create empty board.
            print_board: Used to print empty Board as matrix 3 x 3. #czy to tak ma być?
            print_instr: Used to mark fields(?) by proper numbers.
            """

    def __init__(self):
        self.board = Board.create_empty_board()

    @staticmethod  #odpowiada do całej klasy, a nie do instancji
    def create_empty_board():
        empty_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        return empty_board

    def print_board(self):
        print("{} | {} | {}\n{} | {} | {}\n{} | {} | {}\n".format(self.board[0][0], self.board[0][1], self.board[0][2],
                                                                  self.board[1][0], self.board[1][1], self.board[1][2],
                                                                  self.board[2][0], self.board[2][1], self.board[2][2]))
    @staticmethod
    def print_instr():
        print("{} | {} | {}\n{} | {} | {}\n{} | {} | {}\n".format(1, 2, 3, 4, 5, 6, 7, 8, 9))


