from State import State
from Tree import Node


def print_tree_console(root: Node, prefix="", child_prefix=""):
    if root is None:
        return

    children: list[Node] = root.get_Childern()
    if root.get_isPruned():
        print(prefix, root.get_value(), "(Pruned)")
    else:
        print(prefix, root.get_value())

    sz = len(children)
    for i in range(sz):
        if i < sz - 1:
            print_tree_console(children[i], child_prefix + "├── ", child_prefix + "│   ")
        else:
            print_tree_console(children[i], child_prefix + "└── ", child_prefix + "    ")


def print_count(self):
    print(self.count)