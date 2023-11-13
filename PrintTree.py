from Tree import Node


class PrintTree:
    count = 0  # number of nodes

    def print_tree_console(self, root: Node,prefix="", child_prefix=""):
        if root is None:
            return
        self.count += 1
        children = root.get_Childern()  #get root's children
        print(root, " ")
        sz = len(children)
        for i in range(sz):
            if i < sz - 1:
                self.print_tree_console(children[i], child_prefix+"├── ",child_prefix+"│   ")
            else:
                self.print_tree_console(children[i],child_prefix + "└── ", child_prefix + "    ")

    def print_count(self):
        print(self.count)
