def add(*args):
    total = 0
    for a in args:
        total += a
    return total

def sub(*args):
    if not args:
        raise ValueError("sub requires at least one argument")
    if len(args) == 1:
        return -args[0]
    initial = args[0]
    for n in args[1:]:
        initial -= n
    return initial
