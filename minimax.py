from State import State
import math
import copy

def generate_children(state, player):
    children = []
    for move in state.possible_moves:
        new_State = copy.deepcopy(state)
        new_State.make_move(move, player)
        children.append((new_State, move))
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
        for child, used_move in children:
            child_eval, child_move = minimax(child,  False)
            if child_eval > eval:
                eval = child_eval
                move = used_move
    else:
        eval = math.inf
        for child, used_move in children:
            child_eval, child_move = minimax(child,  True)
            if child_eval < eval:
                eval = child_eval
                move = used_move

    return (eval, move)


def alpha_beta_search(starting_position: State, maxPlayer: bool, alpha=- math.inf, beta=math.inf):
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
        for child, used_move in children:
            child_eval, child_move = alpha_beta_search(child,  False, alpha, beta)
            if child_eval > eval:
                eval = child_eval
                move = used_move
            # update alpha to the best evaluation of a child that has been found
            alpha = max(alpha, child_eval)
            if beta <= alpha:
                # cut off branch since it will not be picked
                break
    else:
        eval = math.inf
        for child, used_move in children:
            child_eval, child_move = alpha_beta_search(child,  True, alpha, beta)
            if child_eval < eval:
                eval = child_eval
                move = used_move
            beta = min(beta, child_eval)
            if beta <= alpha:
                break

    return (eval, move)


def main():
    game = State()
    game.print_board()

    print(minimax(game,maxPlayer=True))
    print(alpha_beta_search(game, True, - math.inf, math.inf))


if __name__ == "__main__":
    main()

