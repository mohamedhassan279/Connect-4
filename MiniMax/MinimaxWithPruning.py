import math
from Heuristic.Heuristic import Heuristic
from State import State
from Tree import Node
from MiniMax.Minimax import Minimax


class MinimaxWithPruning(Minimax):

    def __init__(self, heuristic: Heuristic):
        self.heuristic = heuristic
        self.nodesExpanded = 0

    def get_best_move(self, state, max_depth):
        """
         -> the function that our agent will call in order to get the best move
         -> takes: the current state, and the maximum depth as parameters
         -> returns: the col to play in,
                     the score of this best state, and a pointer to the minimax tree rooted at the passed state whose depth is max_depth, or smaller
                     if the game will end after some levels < max_depth
         """
        root = Node(-1)
        self.nodesExpanded = 0
        score = self.__max_value(state, math.inf * -1, math.inf, max_depth,
                                 root)  # this score must be equal to root.get_value()
        # now we must pick the state whose value is the maximum in the children list of the root
        children: list[Node] = root.get_Childern()
        best_col = self.get_best_col(children)
        return best_col, score, root, self.nodesExpanded

    def __max_value(self, state: State, alpha, beta, remaining_depth, parent: Node):
        ##############################base cases:###########################################

        if remaining_depth == 0:  # this means that we've reached our pre-defined depth then we return the heuristic of this state
            return self.heuristic.get_score(state)

        successors = state.get_successors()
        self.nodesExpanded += 1

        if len(successors) == 0:  # then it means that the current state has no successors (game completed) so we return its heuristic
            return self.heuristic.get_score(state)

        ##############################end of base cases###########################################

        parent.set_value(math.inf * -1)  # we need to maximize this
        for successor in successors:
            child_node = Node(-1)
            parent.add_child(child_node)  # append this node to be a child of the parent node
            child_node.set_value(self.__min_value(successor, alpha, beta, remaining_depth - 1, child_node))
            parent.set_value(max(child_node.get_value(), parent.get_value()))
            if parent.get_value() >= beta:  # then we prune here, and denote the parent to be pruned
                parent.set_isPruned()
                return parent.get_value()
            alpha = max(alpha, parent.get_value())
        return parent.get_value()

    def __min_value(self, state: State, alpha, beta, remaining_depth, parent: Node):
        ##############################base cases:###########################################

        if remaining_depth == 0:  # this means that we've reached our pre-defined depth then we return the heuristic of this state
            return self.heuristic.get_score(state)

        successors = state.get_successors()
        self.nodesExpanded += 1

        if len(successors) == 0:  # then it means that the current state has no successors (game completed) so we return its heuristic
            return self.heuristic.get_score(state)

        ##############################end of base cases###########################################

        parent.set_value(math.inf)  # we need to minimize this
        for successor in successors:
            child_node = Node(-1)
            parent.add_child(child_node)  # append this node to be a child of the parent node
            child_node.set_value(self.__max_value(successor, alpha, beta, remaining_depth - 1, child_node))
            parent.set_value(min(child_node.get_value(), parent.get_value()))
            if parent.get_value() <= alpha:  # then we prune here, and denote the parent to be pruned
                parent.set_isPruned()
                return parent.get_value()
            beta = min(beta, parent.get_value())
        return parent.get_value()
