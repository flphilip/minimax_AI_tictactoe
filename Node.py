import State
import copy


class Node:
    """
    Node class to represent various states the board can be in connect 5
    """

    def __init__(self, state: State, max_player=True):
        """
        :param state: state of the game, containing the board position and flipping values
        :param parent: parent node of this node
        """
        self.state = state
        self.maxPlayer = max_player
        self.move = state.last_move

    def expand_node(self):
        """
        function that generates all valid children of this node
        :return: list of newly generated child nodes
        """
        children = []
        player = 0 if self.maxPlayer else 1
        for move in self.state.possible_moves:
            new_State = copy.deepcopy(self.state)
            new_State.make_move(move, player)
            children.append(Node(new_State, not self.maxPlayer))
        return children


if __name__ == "__main__":
    state = State.State()
    test = Node(state)
    children = test.expand_node()
    print(len(children))
    for child in children:
        child.state.print_board()
        print("---------------------------------------------------")

    heir = children[0]
    children_2 = heir.expand_node()
    print(len(children_2))