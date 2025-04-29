
class State:
    def __init__(self, position=["  "] * 9):
        if len(position) != 9:
            raise Exception("Invalid position was entered")
        self.position = position
        self.winner = None
        self.possible_moves = [i for i in range(9)]
        self.last_move = None
        self.draw = False
        self.is_terminal = False

    def make_move(self, pos, player:str):
        if pos not in self.possible_moves:
            raise Exception("Invalid move")

        self.last_move = pos
        self.position[pos] = player
        self.possible_moves.remove(pos)
        if self.possible_moves == []:
            self.is_terminal = True
            self.draw = True


       
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

    def print_board(self):
        for i in range(3):
            a = self.position[i*3 + 0]
            b = self.position[i*3 + 1]
            c = self.position[i*3 + 2]
            print(f"{a} | {b} | {c}")
            if i != 2: print("------------")


if __name__ == "__main__":
    felix_game = State()
    felix_game.make_move(8,0)
    felix_game.make_move(4,1)
    felix_game.make_move(6,0)
    felix_game.make_move(7,1)
    felix_game.make_move(5,0)
    felix_game.make_move(1,1)

    print(felix_game.possible_moves)
    felix_game.print_board()
    print(felix_game.winner)