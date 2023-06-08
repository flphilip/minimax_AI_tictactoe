from Helper_functions import *


class State:
    """
    class that represents the state of the 5 wins board \n
    the board is 11 fields wide and 8 fields high \n
    the board can be flipped once per game per player, and they cannot occur consecutively

    TO DO: evaluation function
    """

    def __init__(self, player: int = 1, board: list = None, flipped1: bool = False, flipped2: bool = False, move=None):
        if not board:
            # standard empty board if no other board was specified
            self.board = [[] for _ in range(11)]
        else:
            self.board = board
        # this board is supposed to be a list of lists, one for each column
        # this means that the coordinate (0,0) means the bottom left corner, (0,7) means top left corner
        # encoding: 0 means blank, 1 means occupied by player1, 2 means occupied by player 2

        # these booleans tell which player has already used the flip move respectively
        self.flipped1 = flipped1
        self.flipped2 = flipped2
        if player not in [1, 2]:
            raise Exception("Invalid input")
        self.player = player
        self.move = move
        self.invalid = False  # bool to be set when two flips occur consecutively
        self.possible_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def is_valid(self) -> bool:
        """
        determines validity of given position
        :return: bool
        """
        if self.invalid: return False
        for column in self.board:
            if len(column) > 8: return False
        return True

    def has_won(self):
        if self.move is None: return False
        if self.move == 11:
            # this is the case of the last move being a flip, so we have to test the whole board
            for column in range(len(self.board)):
                for row in range(len(self.board[column])):
                    field = self.board[column][row]
                    if field == 0:
                        continue
                    if not out_of_bounds(column + 4, row):  # look right
                        for index in range(5):
                            if self.board[column + index][row] != field: break
                            return True
                    if not out_of_bounds(column + 4, row + 4):  # look right-up
                        for index in range(5):
                            if self.board[column + index][row + index] != field: break
                            return True
                    if not out_of_bounds(column, row + 4):  # look up
                        for index in range(5):
                            if self.board[column][row + index] != field: break
                            return True

                    if not out_of_bounds(column - 4, row + 4):  # look up-left
                        for index in range(5):
                            if self.board[column - index][row + index] != field: break
                            return True
            return False

        else:
            # this is the case of any other move, meaning we can just check the top value of that column for a win
            field_index_x = self.move
            field_index_y = len(self.board[self.move]) - 1
            field_indices = [field_index_x, field_index_y]
            temporary_board = self.get_padded_board()
            possible_directions = [
                [1, 0],  # right
                [1, -1],  # right_down
                [0, -1],  # down
                [-1, -1],  # down_left
                [-1, 0],  # left
                [-1, 1],  # up_left
                [1, 1]  # up_right
            ]
            for direction in possible_directions:
                if check_direction(field_indices, direction[0], direction[1], temporary_board, self.player):
                    return True
            return False

    def get_padded_board(self):
        temporary_board = self.board
        for index in range(len(temporary_board)):
            # pad with zeros so we can have full rows
            temporary_board[index] = (temporary_board[index] + [0] * 8)[:8]
        return temporary_board

    def __repr__(self) -> str:

        string = ""
        for column in self.board:
            # pad the list with zeros and cut off at the 8th digit
            column = (column + [0] * 8)[:8]
            string += str(column)
            string += "\n"
        return string

    def throw_in(self, column: int):
        self.move = column
        self.board[column].append(self.player)
        self.player = 1 if self.player == 2 else 2

    def flipped(self, player) -> bool:
        if player == 1: return self.flipped1
        if player == 2: return self.flipped2

    def flip(self):
        if self.move == 11:
            # two consecutive flips are not allowed and this will be found in the is_valid function
            self.invalid = True
        for column in range(len(self.board)):
            # to flip, since this version has only actual values and no gaps, we simply need to reverse the columns
            self.board[column] = self.board[column][::-1]

        # handle flipping bools for future moves
        if self.player == 1:
            self.flipped1 = True
            self.player = 2
        else:
            self.flipped2 = True
            self.player = 1
        self.move = 11

    def __eq__(self, other):
        result = self.board == other.board and self.player == other.player and self.flipped1 == other.flipped1
        result = result and self.flipped2 == other.flipped2
        return result

    def evaluate(self):
        # Ideas for evaluation:
        # pass the last move to the function, and then perform hasWon with that specific move in mind to save time
        # if the last move was flip, then you probably have to check the whole board
        # if no one has won, perform generic static evaluation as follows:
        # identify all occurrences of 0 adjacent to other values. if it is next to a 1, eval_max +1, and vice versa
        # return eval_max - eval_min

        # is this a good evaluation? probably better than the first attempt but still probably bad

        pass

    def __hash__(self):
        return self.player  + sum(self.board[0])

    def evaluate_position(self):
        return 0
