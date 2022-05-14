from typing import List
from merge_sort import merge_sort


class Node:
    """BST node"""

    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left, self.right = left, right

    def _is_balanced(self):
        if self == None:
            return True
        this_node = abs(Node._height(self.left) - Node._height(self.right)) <= 1
        # a Node is balanced if the difference in height for its branches and
        # all its sub-branches is no more than 1
        return (
            this_node and Node._is_balanced(self.left) and Node._is_balanced(self.right)
        )

    def _balance(self):
        # returns new Node tree
        if self == None:
            return self
        self.left, self.right = Node._balance(self.left), Node._balance(self.right)
        while not self._is_balanced():
            if Node._height(self.right) > Node._height(self.left):
                m = self.right._min_node()
                self.right = self.right._remove(m.label)
                self.left = Node(self.label, self.left, None)
                self.label = m.label
            else:
                m = self.left._max_node()
                self.left = self.left._remove(m.label)
                self.right = Node(self.label, None, self.right)
                self.label = m.label
            # fix branches if higher changes unbalance them
            if not self.left._is_balanced():
                self.left = Node._balance(self.left)
            if not self.right._is_balanced():
                self.right = Node._balance(self.right)
        return self

    def _find(self, v, h=0):
        """Returns the Node with value v and its height, if v exists in the Tree"""
        if self == None:
            raise ValueError(f"{v} not in Tree")
        elif v == self.label:
            return (self, h)
        elif v < self.label:
            return Node._find(self.left, v, h + 1)
        elif v > self.label:
            return Node._find(self.right, v, h + 1)

    def _height(self, h=0):
        if self == None:
            return 0
        return max(h, Node._height(self.left, h + 1), Node._height(self.right, h + 1))

    def _max_node(self):
        if self.right is None:
            return self
        return Node._max_node(self.right)

    def _min_node(self):
        if self.left is None:
            return self
        return Node._min_node(self.left)

    def _remove(self, v):
        # returns new tree
        if self is None:
            return None
        elif v < self.label:
            self.left = Node._remove(self.left, v)
        elif v > self.label:
            self.right = Node._remove(self.right, v)
        else:  # v == self.label
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            m = self.right._min_node()
            self.label = m.label
            self.right = Node._remove(self.right, self.label)
        return self

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
        # if self.left:
        left = ", " + repr(self.left)
        # else:
        #     left = ""
        # if self.right:
        right = ", " + repr(self.right)
        # else:
        #     right = ""
        return "Node(" + repr(self.label) + left + right + ")"

    def __str__(self, h=0):
        if self is None:
            return ""
        left, right = Node.__str__(self.left, h + 1), Node.__str__(self.right, h + 1)
        return left + " " * 3 * h + str(self.label) + "\n" + right


class Tree:
    """Container class for Node with interface"""

    def __init__(self, vals):
        """Constructor. Accepts a List of values or a Node tree for vals."""
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

    def balance(self):
        """Balance the Tree, if it is unbalanced."""
        self.root = self.root._balance()

    def find(self, v):
        """Return the node with the label value v, if it exists.
        Raises an exception if the value is not found."""
        return self.root._find(v)[0]

    def height_of(self, v):
        """Returns the height of the branch containing v.
        Raises an exception if the value is not found."""
        return self.root._find(v)[1]

    @property
    def height(self):
        """Returns the height of the tallest branch of the Tree."""
        return self.root._height()

    def insert(self, v):
        """Insert a Node with the label value v into self"""

        def insert(n, v):
            # mutates
            if v == n.label:
                # do nothing if v already present in Tree
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
        """Remove a Node with the label value v from self"""
        self.root = self.root._remove(v)

    def level_order(self, h):
        """Return an ordered list of all the Nodes in the Tree at height h."""

        def level_order(n, l):
            if n == None:
                raise ValueError(f"no nodes at level {l}")
            if l == 0:
                yield n.label
            else:
                yield from level_order(n.left, l - 1)
                yield from level_order(n.right, l - 1)

        return level_order(self.root, h)

    def inorder(self):
        """Return an ordered list of all the nodes in the tree"""

        def inorder(n):
            if n == None:
                return
            else:
                yield from inorder(n.left)
                yield n.label
                yield from inorder(n.right)

        return inorder(self.root)

    def preorder(self):
        """Return a preordered list of all the Nodes in the Tree."""

        def preorder(n):
            if n == None:
                return
            else:
                yield n.label
                yield from preorder(n.left)
                yield from preorder(n.right)

        return preorder(self.root)

    def postorder(self):
        """Return a postordered list of all the Nodes in the Tree."""

        def postorder(n):
            if n == None:
                return
            else:
                yield from postorder(n.left)
                yield from postorder(n.right)
                yield n.label

        return postorder(self.root)

    def __repr__(self):
        return "Tree(" + repr(self.root) + ")"

    def __str__(self):
        return str(self.root)


if __name__ == "__main__":
    import random

    print("Building Tree with 100 random integers 0-99.")
    t = Tree([random.randint(0, 99) for _ in range(100)])
    print("Built:", t.__repr__())
    print("Balanced? ", t.root._is_balanced())
    print("In order:", list(t.inorder()))
    print("Pre-order:", list(t.preorder()))
    print("Post-order:", list(t.postorder()))
    print()
    print("Adding 100 more random integers.")
    [t.insert(random.randint(50, 150)) for _ in range(100)]
    print("Tree:", t.__repr__())
    print("Balanced?", t.root._is_balanced())
    print("Attempting to balance...")
    t.balance()
    print("Balanced?", t.root._is_balanced())

    from time import time

    def timer_func(func):
        # This function shows the execution time of
        # the function object passed
        def wrap_func(*args, **kwargs):
            t1 = time()
            result = func(*args, **kwargs)
            t2 = time()
            print(f"Function {func.__name__!r} executed in {(t2-t1):.4f}s")

        return wrap_func

    t = Tree([random.randint(0, 99) for _ in range(100)])
    [t.insert(random.randint(50, 150)) for _ in range(100)]
    print(timer_func(t.balance)())
    t = Tree([random.randint(0, 99) for _ in range(100)])
    [t.insert(random.randint(50, 150)) for _ in range(100)]
    print(timer_func(Tree)(list(t.inorder())))
