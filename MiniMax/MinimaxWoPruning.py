import math
import Heuristic.Heuristic
from State import State
from Tree import Node
from MiniMax.Minimax import Minimax


class MinimaxWoPruning(Minimax):
    def __init__(self, heuristic):
        self.__heuristic: Heuristic = heuristic

    def get_best_move(self, state, max_depth):
        """
         -> the function that our agent will call in order to get the best move
         -> takes: the current state, and the maximum depth as parameters
         -> returns: the col to play in,
                     the score of this best state, and a pointer to the minimax tree rooted at the passed state whose depth is max_depth, or smaller
                     if the game will end after some levels < max_depth
         """
        root = Node(-1)
        score = self.__max_value(state, max_depth, root)  # this score must be equal to root.get_value()
        # now we must pick the state whose value is the maximum in the children list of the root
        children: list[Node] = root.get_Childern()
        best_col = self.get_best_col(children)
        return best_col, score, root

    def __min_value(self, state: State, max_depth: int, root: Node):
        if max_depth == 0:  # terminal state
            return self.__heuristic.get_score(state)
        children = state.get_successors()
        if len(children) == 0:  # no children
            return self.__heuristic.get_score(state)
        root.set_value(math.inf)  # initially infinity
        for s in children:
            child = Node(-1)  # make new node initially its value=-1
            root.add_child(child)  # add it to the search tree
            child.set_value(self.__max_value(s, max_depth - 1, child))
            root.set_value(min(root.get_value(), child.get_value()))
        return root.get_value()

    def __max_value(self, state: State, max_depth: int, root: Node):
        if max_depth == 0:  # terminal state
            return self.__heuristic.get_score(state)
        children = state.get_successors()
        if len(children) == 0:  # no children
            return self.__heuristic.get_score(state)
        root.set_value(-math.inf)  # initially -infinity
        for s in children:
            child = Node(-1)  # make new node initially its value=-1
            root.add_child(child)  # add it to the search tree
            child.set_value(self.__min_value(s, max_depth - 1, child))
            root.set_value(max(root.get_value(), child.get_value()))
        return root.get_value()
