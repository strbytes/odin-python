from typing import List
from merge_sort import merge_sort


class Node:
    # BST node
    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left, self.right = left, right

    def _min_node(self):
        if self.left is None:
            return self
        return Node._min_node(self.left)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.label == other.label
        else:
            return self.label == other

    def __lt__(self, other):
        if isinstance(other, Node):
            return self.label < other.label
        else:
            return self.label < other

    def __gt__(self, other):
        if isinstance(other, Node):
            return self.label > other.label
        else:
            return self.label > other

    def __repr__(self):
        if self.left:
            left = ", " + repr(self.left)
        else:
            left = ""
        if self.right:
            right = ", " + repr(self.right)
        else:
            right = ""
        return "Node(" + repr(self.label) + left + right + ")"

    def __str__(self):
        if self.left:
            left = ", " + str(self.left)
        else:
            left = ""
        if self.right:
            right = ", " + str(self.right)
        else:
            right = ""
        return "(" + str(self.label) + left + right + ")"


class Tree:
    # Container class for Node with interface
    def __init__(self, vals):
        if isinstance(vals, Node):
            self.root = vals
        if isinstance(vals, List):
            # use a sorted list to build a balanced tree
            lst = merge_sort(list(set(vals)))
            self.root = self._build_tree(lst)

    def _build_tree(self, lst):
        """Build a balanced tree out of a list passed to the constructor"""
        if not lst:
            return None
        left, right = lst[: len(lst) // 2], lst[len(lst) // 2 :]
        # choose from larger list (or left if equal) and remove duplicates
        if right and len(left) < len(right):
            label = right[0]
            del right[0]
        else:
            label = left[-1]
            del left[-1]
        node = Node(label)
        node.left = self._build_tree(left)
        node.right = self._build_tree(right)
        return node

    def insert(self, v):
        """Insert a value v into self"""

        def insert(n, v):
            # mutates
            if v == n.label:
                return
            if v < n.label:
                if n.left:
                    insert(n.left, v)
                else:
                    n.left = Node(v)
            else:
                if n.right:
                    insert(n.right, v)
                else:
                    n.right = Node(v)

        insert(self.root, v)

    def remove(self, v):
        """Remove a value v from self"""

        def remove(n, v):
            # returns new tree
            if n is None:
                return None
            elif v < n.label:
                n.left = remove(n.left, v)
            elif v > n.label:
                n.right = remove(n.right, v)
            else:  # v == n.label
                if n.left is None:
                    n, temp = None, n.right
                    return temp
                elif n.right is None:
                    n, temp = None, n.left
                    return temp
                m = n.right._min_node()
                n.label = m.label
                n.right = remove(n.right, n.label)
            return n

        self.root = remove(self.root, v)

    def __repr__(self):
        return "Tree(" + repr(self.root) + ")"

    def __str__(self):
        return str(self.root)
