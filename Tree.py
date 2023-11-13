import State


class Node:


    def __init__(self, value):
        self.value = value      # the value of the node obtained from Minimax algorithm
        self.successors = []    # to store the successors of the node as array of Node
        self.is_pruned = False  # to indicate that this node has been pruned

    def add_child(self, child):
        self.successors.append(child)

    def get_Childern(self) -> list:
        return self.successors

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_isPruned(self):
        self.is_pruned = True

    def get_isPruned(self):
        return self.is_pruned
