RED = "\x1b[91m"
BLUE = "\x1b[94m"
ENDC = "\x1b[0m"
# ]]] Treesitter thinks the brackets in the quotes are code and is indenting based on them -_-;


class Board:
    def __init__(self):
        self.plays = {i: [] for i in range(7)}
