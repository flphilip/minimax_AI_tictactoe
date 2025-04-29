from State import State
import math
import copy


def alpha_beta_search(starting_position, alpha, beta):
    pass

def generate_children(state, player):
    """
    function that generates all valid children of this node
    :return: list of newly generated child nodes
    """
    children = []
    for move in state.possible_moves:
        new_State = copy.deepcopy(state)
        new_State.make_move(move, player)
        children.append(new_State)
    return children

def minimax(starting_position: State, maxPlayer):
    if starting_position.is_terminal:
        if starting_position.draw:
            return (0, starting_position.last_move)

        winner = starting_position.winner
        if (winner == 0):
            return (1, starting_position.last_move)  
        else:
            return (-1, starting_position.last_move) 
    player = "O" if maxPlayer else "X"
    children = generate_children(starting_position, player)
    move = -1

    if maxPlayer:
        eval = -math.inf
        for child in children:
            child_eval, child_move = minimax(child, not maxPlayer)
            if child_eval > eval:
                eval = child_eval
                move = child_move
    else:
        eval = math.inf
        for child in children:
            child_eval, child_move = minimax(child, not maxPlayer)
            if child_eval < eval:
                eval = child_eval
                move = child_move

    return (eval, move)


            
    
def main():

    game = State()
    # game.make_move(8,"O")
    # game.make_move(4,"X")
    # game.make_move(5,"O")
    # game.make_move(2,"X")
    # game.make_move(6,"O")
    # game.make_move(0,"X")
    # # game.make_move(1,"O")

    print("Winner", game.winner)
    game.print_board()

    print(minimax(game,maxPlayer=True))
    # print(alpha_beta_search(begin, 2, - math.inf, math.inf))


if __name__ == "__main__":
    main()

