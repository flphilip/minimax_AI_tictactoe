
class State:
    def __init__(self, position=["-1"] * 9):
        if len(position) != 9:
            raise Exception("Invalid position was entered")
        self.position = position
        self.player = 1
        self.winner = None
        self.possible_moves = [i for i in range(9)]
        self.last_move = None

    def make_move(self, pos, debug_player = None):
        if pos not in self.possible_moves:
            raise Exception("Invalid move")
        if debug_player:
            player = debug_player
        else:
            player = self.player
            self.player = (self.player - 1) % 2
        self.last_move = pos
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
            self.winner = player

    def print_board(self):
        for i in range(3):
            a = self.position[i*3 + 0]
            b = self.position[i*3 + 1]
            c = self.position[i*3 + 2]
            print(f"{a} | {b} | {c}")
            if i != 2: print("----------")


if __name__ == "__main__":
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