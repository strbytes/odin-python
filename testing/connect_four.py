RED = "\x1b[91m"
BLUE = "\x1b[94m"
ENDC = "\x1b[0m"
# ]]] Treesitter thinks the brackets in the quotes are code and is indenting based on them -_-;


class Board:
    def __init__(self):
        self.plays = {i: [] for i in range(7)}

    def add_play(self, column, color):
        if type(column) is not int:
            raise ValueError(f"add_play accepts integers as input, not {type(column)}")
        if column < 0 or column > 6:
            raise ValueError(f"column {column} is out of bounds")
        if color not in (RED, BLUE):
            raise ValueError(f"invalid color input {color}")
        if len(self.plays[column]) >= 6:
            raise ValueError(f"column {column} is full")
        self.plays[column].append(color)

    def __str__(self):
        board = ""
        for y in reversed(range(6)):
            for x in range(7):
                try:
                    board += self.plays[x][y] + "⚫" + ENDC
                except IndexError:
                    board += ". "
            board += "\n"
        board += "1 2 3 4 5 6 7 "
        return board
