from Node import Node
from State import State
import math


# def alpha_beta_search(parent_node: Node, depth: int, alpha, beta):
#     """
#     subroutine intended to be used in an iterative deepening search for minimax algorithm
#     :param known:
#     :param parent_node:
#     :param depth:
#     :param alpha:
#     :param beta:
#     :return:
#     """

#     if parent_node.state.winner is not None():
#         return [10_000, parent_node.state.move] \
#             if parent_node.state.player == 2 \
#             else [-10_000, parent_node.state.move]
#     if depth == 0:
#         return [parent_node.state.evaluate_position(), parent_node.state.move]
#     children = parent_node.expand_node()
#     if parent_node.maxPlayer:
#         value = - math.inf
#         move = -1

#         for child in children:
#             child_eval = alpha_beta_search(child, depth - 1, alpha, beta)
#             if child_eval[0] > value:
#                 value = child_eval[0]
#                 move = child_eval[1]

#             alpha = max(alpha, value)
#             if value >= beta:
#                 break
#         return [value, move]
#         # if node depth = max depth of this iteration: return evaluation of position (base case)
#         # else expand node into its children and append to a queue. queue = expand_node(parent_node, 1)
#         # sort them in a way so that nodes that are most likely to be good moves are explored first
#         # for the pruning to work better (no idea what moves are likely to be good yet)
#         # return max of the dfs search result for its children in recursive call
#         # and write move to a txt file I guess, this may cause a problem if every recursive call does this
#     else:
#         # basically the same but you expand nodes for player 2 and look for the minimum of the recursive calls
#         value = math.inf
#         move = -1
#         for child in children:
#             child_eval = alpha_beta_search(child, depth - 1, alpha, beta)
#             if child_eval[0] < value:
#                 value = child_eval[0]
#                 move = child_eval[1]
#             beta = min(beta, value)
#             if value <= alpha:
#                 break
#         return [value, move]


# def iterative_deepening_search(start: Node, max_depth: int):
#     evaluation = 0
#     move = -1
#     for iteration in range(1, max_depth):
#         evaluation, move = alpha_beta_search(start, iteration, -math.inf, math.inf)
#         # future: write this to a txt file
#     return evaluation, move

def minimax(starting_node: Node):
    # basic implementation of minimax without alpha beta pruning
    has_won = starting_node.state.winner
    max_player = starting_node.maxPlayer
    # return the inverse because in this case the last move was important
    if has_won: return (-1 if max_player else 1, starting_node.move)

    children = starting_node.expand_node()
    move = -1
    if max_player:
        eval = -math.inf
        for child in children:
            child_eval, child_move = minimax(child)
            move = child_move if child_eval > eval else move
            eval = max(eval, child_eval)
    else:
        eval = math.inf
        for child in children:
            child_eval, child_move = minimax(child)
            move = child_move if child_eval < eval else move
            eval = min(eval, child_eval)

    return (eval, move)

            
    
def main():
    a = State()
    begin = Node(a)
    
    ending_position = State()
    ending_position.make_move(0)
    ending_position.make_move(3)
    ending_position.make_move(1)
    ending_position.make_move(4)
    ending_position.make_move(5)
    ending = Node(ending_position)

    print(minimax(begin))
    # print(alpha_beta_search(begin, 2, - math.inf, math.inf))


if __name__ == "__main__":
    main()

