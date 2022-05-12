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
        if i < 0:
            l = len(self)
            i = l + i
            if i > l:
                raise IndexError("Node index out of range")
        if self.rest == Node.empty and i > 0:
            raise IndexError("Node index out of range")
        if i == 0:
            return self
        return Node._traverse(self.rest, i - 1)

    def __str__(self, new=True, start="(", delimit=" ", declose="", end=")"):
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
            value = str(self.first)
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
    def __init__(self):
        self.head = Node.empty

    def __len__(self):
        if self.head is Node.empty:
            return 0
        return len(self.head)

    def append(self, value):
        if self.head is Node.empty:
            self.head = Node(value)
        else:
            n = self.head._traverse(len(self.head) - 1)
            n.rest = Node(value, n.rest)

    def prepend(self, value):
        self.head = Node(value, self.head)

    def __str__(self):
        return str(self.head)

    def __repr__(self):
        return self.head.__repr__()


if __name__ == "__main__":
    a = Link()
    for i in range(3):
        a.append(i)
