class Node:
    empty = ()

    def __init__(self, first, rest=empty):
        assert (
            isinstance(rest, Node) or rest == Node.empty
        ), "rest must be Node or empty list"
        self.first, self.rest = first, rest

    def __len__(self):
        if self is Node.empty:
            return 0
        return 1 + len(self.rest)

    def _traverse(self, i):
        if isinstance(i, slice):
            raise NotImplementedError("slices not implemented for Link/Node")
        if i < 0:
            l = len(self)
            i = l + i
            if i < 0:
                raise IndexError("Node index out of range")
        if self.rest == Node.empty and i > 0:
            raise IndexError("Node index out of range")
        if i == 0:
            return self
        return Node._traverse(self.rest, i - 1)

    def __str__(self, new=True, start="(", delimit=", ", declose="", end=")"):
        if self is Node.empty:
            return end
        if isinstance(self.first, Node):
            value = Node.__str__(
                self.first,
                new=True,
                start=start,
                delimit=delimit,
                declose=declose,
                end=end,
            )
        else:
            value = repr(self.first)
        use_start = start if new else ""
        use_delimit = delimit if self.rest else ""
        use_declose = declose if self.rest else ""
        return (
            use_start
            + value
            + use_delimit
            + Node.__str__(
                self.rest,
                new=False,
                start=start,
                delimit=delimit,
                declose=declose,
                end=end,
            )
            + use_declose
        )

    def __repr__(self):
        return self.__str__(start="Node(", delimit=", Node(", declose=")", end=")")


class Link:
    def __init__(self, *args):
        self.head = Node.empty
        for item in reversed(args):
            self.head = Node(item, self.head)

    def insert(self, i, v):
        l = self.head._traverse(i)
        l.rest = Node(l.first, l.rest)
        l.first = v

    def append(self, value):
        if self.head is Node.empty:
            self.head = Node(value)
        else:
            n = self.head._traverse(len(self.head) - 1)
            n.rest = Node(value, n.rest)

    def prepend(self, value):
        self.head = Node(value, self.head)

    def pop(self):
        if self.head == Node.empty:
            raise IndexError("pop from empty list")
        if len(self) == 1:
            v = self.head.first
            self.head = Node.empty
            return v
        l = self.head._traverse(-2)
        v = l.rest.first
        l.rest = Node.empty
        return v

    def __delitem__(self, i):
        if i >= len(self):  # Check for index 0 on empty list or i == len(self)
            raise IndexError("Link index out of range")
        elif i == 0:
            self.head = self.head.rest
        else:
            l = self.head._traverse(i - 1)
            l.rest = l.rest.rest

    def __getitem__(self, i):
        l = self.head._traverse(i)
        return l.first

    def __setitem__(self, i, v):
        l = self.head._traverse(i)
        l.first = v

    def __len__(self):
        if self.head is Node.empty:
            return 0
        return len(self.head)

    def __str__(self):
        return str(self.head)

    def __repr__(self):
        return "Link" + str(self)


if __name__ == "__main__":
    a = Link(1, 2, 3)
