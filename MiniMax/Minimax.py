import abc
import math
from Tree import Node


class Minimax(object):
    def get_best_col(self, children: list[Node]):
        best_col, max_score = 0, math.inf * -1
        for i in range(len(children)):
            if children[i].get_value() > max_score:
                max_score = children[i].get_value()
                best_col = i  # where the best col is the col number of non-full columns
        return best_col

    @abc.abstractmethod
    #the only function that's public
    def get_best_move(self, state, max_depth):
        pass
