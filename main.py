from Node import Node
from State import State
import math


def alpha_beta_search(starting_node: Node, alpha, beta):
    pass

def minimax(starting_node: Node):
    max_player = starting_node.maxPlayer
    if starting_node.state.is_terminal:
        if starting_node.state.draw:
            return (0, starting_node.move)

        winner = starting_node.state.winner
        if (winner == 0):
            return (1, starting_node.move)  
        else:
            return (-1, starting_node.move) 

    children = starting_node.expand_node()
    move = -1

    if max_player:
        eval = -math.inf
        for child in children:
            child_eval, child_move = minimax(child)
            if child_eval > eval:
                eval = child_eval
                move = child_move
    else:
        eval = math.inf
        for child in children:
            child_eval, child_move = minimax(child)
            if child_eval < eval:
                eval = child_eval
                move = child_move

    return (eval, move)


            
    
def main():

    game = State()
    game.make_move(8,0)
    game.make_move(4,1)
    game.make_move(6,0)
    game.make_move(7,1)
    game.make_move(5,0)
    game.make_move(1,1)

    print("Winner", game.winner)
    game.print_board()

    game_node = Node(game, True)
    print(minimax(game_node))
    # print(alpha_beta_search(begin, 2, - math.inf, math.inf))


if __name__ == "__main__":
    main()

