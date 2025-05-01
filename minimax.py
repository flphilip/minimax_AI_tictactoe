from State import State
import math
import copy


def alpha_beta_search(starting_position, alpha, beta):
    pass

def generate_children(state, player):
    children = []
    for move in state.possible_moves:
        new_State = copy.deepcopy(state)
        new_State.make_move(move, player)
        children.append(new_State)
    return children


def minimax(starting_position: State, maxPlayer: bool):
    if starting_position.is_terminal:
        if starting_position.draw:
            return (0, starting_position.last_move)
        winner = starting_position.winner
        if (winner == "X"):
            return (1, starting_position.last_move)  
        else:
            return (-1, starting_position.last_move) 
    next_player = "X" if maxPlayer else "O"
    children = generate_children(starting_position, next_player)
    move = -1

    if maxPlayer:
        eval = -math.inf
        for child in children:
            child_eval, child_move = minimax(child,  False)
            if child_eval > eval:
                eval = child_eval
                move = child_move
    else:
        eval = math.inf
        for child in children:
            child_eval, child_move = minimax(child,  True)
            if child_eval < eval:
                eval = child_eval
                move = child_move

    return (eval, move)


def main():
    game = State()
    game.make_move(8,"O")
    game.make_move(4,"X")
    game.make_move(7,"O")
    game.make_move(6,"X")
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

    print(minimax(game,maxPlayer=True))
    # print(alpha_beta_search(begin, 2, - math.inf, math.inf))


if __name__ == "__main__":
    main()

