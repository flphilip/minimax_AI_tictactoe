import State
import copy


class Node:
    """
    Node class to represent various states the board can be in connect 5
    """

    def __init__(self, state: State, parent=None):
        """
        :param state: state of the game, containing the board position and flipping values
        :param parent: parent node of this node
        """
        self.state = state
        self.maxPlayer = True if self.state.player == 1 else False
        self.parent = parent
        self.children = []
        self.move = state.move

    def expand_node(self):
        """
        function that generates all valid children of this node
        :return: list of newly generated child nodes
        """
        children = []
        for move in self.state.possible_moves:
            new_State = copy.deepcopy(self.state)
            new_State.make_move(move)
            children.append(Node(new_State, self))
        return children
