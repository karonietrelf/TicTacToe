from Player import Player
from Board import Board
import random

class Game:
    """Class to represent a Game.

        Attributes:
            player1: A name of the first Player.
            player2: A name of the second Player.
            board1: Variable which stores Board.
            next_move: Variable which stores players, who will be doing next move.
            winner: Player who wins the Game.
            is_tie: Variable which stores information is the game ended in tie.
        Methods:
        get_random: Static method. Used to get random number from 0 to 1.
        make_move: Used to ask player to enter a number form 1-9 to set sign in proper field.
        is_game_over: Used to check if there is a winner or a tie.
        check_tie: Returns True when there is no blank field left and no winner. Otherwise False.
        check_winner: Cheeks if there is a winner and assign next_move player to winner parameter.
        start_game: Used to call appropriate methods to play a game. Returns when winner != None or is_tie = True
        show_instruction: Static method.Used to print instruction.
        change_player: Used to change next_move parameter.
        save_data: Used to append data to text file.
        """

    def __init__(self):
        self.player1 = Player(player_name=input("Please enter first player's name: "))
        self.player2 = Player(player_name=input("Please enter second player's name: "))
        self.board1 = Board()
        self.next_move = None
        self.winner = None
        self.is_tie = False

        if Game.get_random() <= 0.5:
            self.player1.set_sign(player_sign="O")
            self.player2.set_sign(player_sign="X")
            self.next_move = self.player1
        else:
            self.player1.set_sign(player_sign="X")
            self.player2.set_sign(player_sign="0")
            self.next_move = self.player2

    @staticmethod
    def get_random():
       return random.randint(0, 1)

    def make_move(self):
        b = self.board1.board
        enter_number = 0
        while True:
            try:
                while enter_number not in range(1, 10):
                    self.board1.print_board()
                    enter_number = int(input("{} please enter number(1-9): ".format(self.next_move.name)))
                    if enter_number not in range(1, 10):
                        print("You've entered {}. The value should be in range (1-9)".format(enter_number))
                if b[0][0] == " " and enter_number == 1:
                    self.board1.board[0][0] = self.next_move.get_sign()
                elif b[0][1] == " " and enter_number == 2:
                    self.board1.board[0][1] = self.next_move.get_sign()
                elif b[0][2] == " " and enter_number == 3:
                    self.board1.board[0][2] = self.next_move.get_sign()
                elif b[1][0] == " " and enter_number == 4:
                    self.board1.board[1][0] = self.next_move.get_sign()
                elif b[1][1] == " " and enter_number == 5:
                    self.board1.board[1][1] = self.next_move.get_sign()
                elif b[1][2] == " " and enter_number == 6:
                    self.board1.board[1][2] = self.next_move.get_sign()
                elif b[2][0] == " " and enter_number == 7:
                    self.board1.board[2][0] = self.next_move.get_sign()
                elif b[2][1] == " " and enter_number == 8:
                    self.board1.board[2][1] = self.next_move.get_sign()
                elif b[2][2] == " " and enter_number == 9:
                    self.board1.board[2][2] = self.next_move.get_sign()
                else:
                    self.board1.print_board()
                    print("Please enter correct value.")
                    enter_number = -1
                    continue
                break
            except ValueError:
                self.board1.print_board()
                print("Please enter a correct value.")

    def is_game_over(self):
        if self.winner != None or self.is_tie == True:
            return True
        else:
            return False

    def check_tie(self):
        for row in self.board1.board:
            for item in row:
                if item == " ":
                    self.is_tie = False
                    return
        self.is_tie = True

    def check_winner(self):
        b = self.board1.board
        if b[0][0] == b[0][1] == b[0][2] != " ":
            if b[0][0] == self.player1.get_sign():
                self.winner = self.player1
            else:
                self.winner = self.player2
        elif b[1][0] == b[1][1] == b[1][2] != " ":
            if b[1][0] == self.player1.get_sign():
                self.winner = self.player1
            else:
                self.winner = self.player2
        elif b[2][0] == b[2][1] == b[2][2] != " ":
            if b[2][0] == self.player1.get_sign():
                self.winner = self.player1
            else:
                self.winner = self.player2
        elif b[0][0] == b[1][0] == b[2][0] != " ":
            if b[0][0] == self.player1.get_sign():
                self.winner = self.player1
            else:
                self.winner = self.player2
        elif b[0][1] == b[1][1] == b[2][1] != " ":
            if b[0][1] == self.player1.get_sign():
                self.winner = self.player1
            else:
                self.winner = self.player2
        elif b[0][2] == b[1][2] == b[2][2] != " ":
            if b[0][2] == self.player1.get_sign():
                self.winner = self.player1
            else:
                self.winner = self.player2
        elif b[0][0] == b[1][1] == b[2][2] != " ":
            if b[0][0] == self.player1.get_sign():
                self.winner = self.player1
            else:
                self.winner = self.player2
        elif b[2][0] == b[1][1] == b[0][2] != " ":
            if b[2][0] == self.player1.get_sign():
                self.winner = self.player1
            else:
                self.winner = self.player2

    def start_game(self):
        self.show_instruction()
        input("Press ENTER to start the game.")
        while not self.is_game_over():
            self.make_move()
            self.change_player()
            self.check_winner()
            self.check_tie()
        if self.is_tie:
            self.board1.print_board()
            print("It's a tie. Game over.")
        else:
            self.board1.print_board()
            print("The winner is {}".format(self.winner.name))
        self.save_data()

    def show_instruction(self):
        print("Hello. Welcome to the Tic Tac Toe game. There are two players. You will see board with numbers. "
              "If you choose field, where you want to put sign, press proper number.")
        Board.print_instr()

    def change_player(self):
        if self.next_move == self.player1:
            self.next_move = self.player2
        else:
            self.next_move = self.player1

    def save_data(self):
        with open("results.txt", "a") as players_results:
            if self.is_tie == True:
                players_results.write("{},1\n".format(self.player1.name))
                players_results.write("{},1\n".format(self.player2.name))
            else:
                players_results.write("{},2\n".format(self.winner.name))
                players_results.write("{},0\n".format(self.next_move.name))


if __name__ == "__main__":
    game1 = Game()
    game1.start_game()
