
class State:
    def __init__(self, position=None):
        if position is None:
            position = [" "] * 9
        if len(position) != 9:
            raise Exception("Invalid position was entered")
        self.position = position
        self.winner = None
        self.possible_moves = [i for i in range(9)]
        self.last_move = None
        self.draw = False
        self.is_terminal = False
        self.current_player = "X"

    def make_move(self, pos):
        if pos not in self.possible_moves:
            raise Exception("Invalid move")

        self.last_move = pos
        player = self.current_player
        self.position[pos] = player
        self.possible_moves.remove(pos)
       
        row_idx = pos // 3
        col_idx = pos % 3
        # row check
        has_won = (self.position[row_idx*3] == self.position[row_idx*3 +1] == self.position[row_idx*3 +2] == player)
        # col check
        has_won |= (self.position[col_idx] == self.position[col_idx+3] == self.position[col_idx+6] == player)
        # diag check
        has_won |= (self.position[0] == self.position[4] == self.position[8] == player)
        has_won |= (self.position[2] == self.position[4] == self.position[6] == player)

        if has_won: 
            self.is_terminal = True
            self.winner = player
            return

        if self.possible_moves == []:
            self.is_terminal = True
            self.draw = True

        self.current_player = "X" if self.current_player == "O" else "O"

    def print_board(self):
        for i in range(3):
            a = self.position[i*3 + 0]
            b = self.position[i*3 + 1]
            c = self.position[i*3 + 2]
            print(f"{a} | {b} | {c}")
            if i != 2: print("-----------")

    def encoding(self):
        st = ""
        for cell in self.position:
            st = st + str(cell)
        return st
    
    def reward(self):
        # for player 2
        if self.winner == "X":
            return -2
        if self.winner == "O":
            return 1
        else: return 0.5


if __name__ == "__main__":
    game = State()
    game.make_move(8,"X")
    print(game.last_move)
    print(game.encoding())
    print(game.possible_moves)
    game.print_board()
    print(game.winner)