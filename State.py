
class State:
   
    def __init__(self):
        self.board = ["-1"] * 9
        self.player = 1
        self.winner = None
        self.possible_moves = [i for i in range(9)]

    def make_move(self, pos, debug_player = None):
        if pos not in self.possible_moves:
            raise Exception("Invalid move")
        if debug_player:
            player = debug_player
        else:
            player = self.player
            self.player = (self.player - 1) % 2
        self.board[pos] = player
        self.possible_moves.remove(pos)


       
        row_idx = pos // 3
        col_idx = pos % 3
        # row check
        has_won = (self.board[row_idx*3] == self.board[row_idx*3 +1] == self.board[row_idx*3 +2] == player)
        # col check
        has_won |= (self.board[col_idx] == self.board[col_idx+3] == self.board[col_idx+6] == player)
        # diag check
        has_won |= (self.board[0] == self.board[4] == self.board[8] == player)
        has_won |= (self.board[2] == self.board[4] == self.board[6] == player)

        if has_won: 
            self.winner = player

    def print_board(self):
        for i in range(3):
            a = self.board[i*3 + 0]
            b = self.board[i*3 + 1]
            c = self.board[i*3 + 2]
            print(f"{a} | {b} | {c}")
            if i != 2: print("----------")

test = State()
test.make_move(2)
test.make_move(4)
test.make_move(3)
test.make_move(8)
test.make_move(6)
test.make_move(0)
print(test.possible_moves)
test.print_board()
print(test.winner)