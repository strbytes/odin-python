class Link:
    # Mostly rebuilding the Link class from Composing Programs
    empty = ()

    def __init__(self, first, rest=empty):
        self.first, self.rest = first, rest

    def append(self, value):
        if self.rest is Link.empty:
            self.rest = Link(value)
        else:
            self.rest.append(value)

    def prepend(self, value):
        self.rest = Link(self.first, self.rest)
        self.first = value

    def __str__(self, new=True, start="(", delimit=" ", declose="", end=")"):
        if self is Link.empty:
            return end
        if isinstance(self.first, Link):
            value = Link.__str__(
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
            + Link.__str__(
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
        return self.__str__(start="Link(", delimit=", Link(", declose=")", end=")")

    def __len__(self):
        if self.rest is Link.empty:
            return 1
        return 1 + Link.__len__(self.rest)

    def head(self):
        return self.first

    def tail(self):
        if self.rest is Link.empty:
            return self.first
        return Link.tail(self.rest)

    def __getitem__(self, i):
        assert i >= 0, "Negative indexing not implemented"
        if self.rest == Link.empty and i > 0:
            raise IndexError(f"Link index out of range")
        if i == 0:
            return self.first
        return Link.__getitem__(self.rest, i - 1)

    def pop(self):
        return self._pophelper(len(self) - 2)

    def _pophelper(self, i):
        if i == 0:
            value = self.rest.first
            self.rest = Link.empty
            return value
        return Link._pophelper(self.rest, i - 1)

    def __contains__(self, value):
        # does not check nested lists
        if self is Link.empty:
            return False
        elif self.first == value:
            return True
        return Link.__contains__(self.rest, value)

    def find(self, value, i=0):
        if self is Link.empty:
            raise ValueError(f"{value} not in linked list")
        if self.first == value:
            return i
        return Link.find(self.rest, value, i + 1)

    def insert(self, value, i):
        if self is Link.empty:
            raise IndexError("Link index out of range")
        if i == 0:
            self.rest = Link(self.first, self.rest)
            self.first = value
        else:
            Link.insert(self.rest, value, i - 1)


def remove(lnk, i):
    # could't figure out how to get this to handle 0 as a method
    if lnk is Link.empty:
        raise IndexError("Link index out of range")
    elif i == 0:
        return lnk.rest
    else:
        return Link(lnk.first, lnk.rest)


if __name__ == "__main__":
    a = Link(1, Link(2, Link(3)))
    a.append(Link(4, Link(5)))
