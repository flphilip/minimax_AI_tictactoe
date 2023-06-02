from Node import Node
from State import State
import math


def alpha_beta_search(parent_node: Node, depth: int, alpha, beta):
    """
    subroutine intended to be used in an iterative deepening search for minimax algorithm
    :param parent_node:
    :param depth:
    :param alpha:
    :param beta:
    :return:
    """
    if parent_node.state.has_won():
        return [10_000, parent_node.state.move] \
            if parent_node.state.player == 1 \
            else [-10_000, parent_node.state.move]
    if depth == 0: return [parent_node.state.evaluate_position(), parent_node.state.move]
    children = parent_node.expand_node()
    if parent_node.maxPlayer:
        value = - math.inf
        move = -1

        for child in children:
            childeval = alpha_beta_search(child, depth - 1, alpha, beta)
            if childeval[0] > value:
                value = childeval[0]
                move = childeval[1]

            alpha = max(alpha, value)
            if value >= beta:
                break
        return [value, move]
        # if node depth = max depth of this iteration: return evaluation of position (base case)
        # else expand node into its children and append to a queue. queue = expand_node(parent_node, 1)
        # sort them in a way so that nodes that are most likely to be good moves are explored first
        # for the pruning to work better (no idea what moves are likely to be good yet)
        # return max of the dfs search result for its children in recursive call
        # and write move to a txt file I guess, this may cause a problem if every recursive call does this
    else:
        # basically the same but you expand nodes for player 2 and look for the minimum of the recursive calls
        value = math.inf
        move = -1
        for child in children:
            childeval = alpha_beta_search(child, depth - 1, alpha, beta)
            if childeval[0] < value:
                value = childeval[0]
                move = childeval[1]
            beta = min(beta, value)
            if value <= alpha:
                break
        return [value, move]


# GENERAL NOTES
# consider making expand node a function of the node class instead of free method


def main():
    a = State()
    begin = Node(a)
    print(alpha_beta_search(begin, 30, - math.inf, math.inf))


if __name__ == "__main__":
    main()

# current problems:
# evaluation function is trash
# has won causes some sort of error on non-specific move location case (not flip)
