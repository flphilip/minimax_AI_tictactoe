from State import State
import math
import copy


def alpha_beta_search(starting_position, alpha, beta):
    pass

def generate_children(state, player):
    children = []
    for move in state.possible_moves:
        new_state = copy.deepcopy(state)
        new_state.make_move(move, player)
        children.append((new_state, move))
    return children


def minimax(starting_position: State, maxPlayer: bool):
    if starting_position.is_terminal:
        if starting_position.draw:
            return (0, starting_position.last_move)
        winner = starting_position.winner
        return (1, starting_position.last_move) if winner == "O" else (-1, starting_position.last_move)

    next_player = "X" if maxPlayer else "O"
    children = generate_children(starting_position, next_player)

    if maxPlayer:
        eval = -math.inf
        best_move = None
        for child_state, move_used in children:
            child_eval, _ = minimax(child_state, False)
            if child_eval > eval:
                eval = child_eval
                best_move = move_used
    else:
        eval = math.inf
        best_move = None
        for child_state, move_used in children:
            child_eval, _ = minimax(child_state, True)
            if child_eval < eval:
                eval = child_eval
                best_move = move_used

    return (eval, best_move)


def main():
    game = State()
    game.make_move(8,"O")
    game.make_move(4,"X")
    game.make_move(7,"O")
    # game.make_move(6,"X")
    # game.make_move(1,"O")
    # game.make_move(0,"X")
    # game.make_move(1,"O")
    # children = generate_children(game, "X")
    # for child in children:
    #     child.print_board()
    #     print(child.last_move)
    #     print(child.winner)
    #     print("------------------------------------")
    print("Winner", game.winner)
    game.print_board()

    print(minimax(game,maxPlayer=False))
    # print(alpha_beta_search(begin, 2, - math.inf, math.inf))


if __name__ == "__main__":
    main()

