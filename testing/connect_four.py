RED = "\x1b[91m"
BLUE = "\x1b[94m"
ENDC = "\x1b[0m"
# ]]] Treesitter thinks the brackets in the quotes are code and is indenting based on them -_-;


class Board:
    def __init__(self):
        self.plays = {i: ["" for _ in range(6)] for i in range(7)}

    def add_play(self, column, color):
        if type(column) is not int:
            raise ValueError(f"add_play accepts integers as input, not {type(column)}")
        if column < 0 or column > 6:
            raise ValueError(f"column {column} is out of bounds")
        if color not in (RED, BLUE):
            raise ValueError(f"invalid color input {color}")
        if self.plays[column][5] != "":
            raise ValueError(f"column {column} is full")
        for y in range(6):
            if self.plays[column][y] == "":
                self.plays[column][y] = color
                break

    def __str__(self):
        board = ""
        for y in reversed(range(6)):
            for x in range(7):
                if self.plays[x][y] != "":
                    board += self.plays[x][y] + "⚫" + ENDC
                else:
                    board += ". "
            board += "\n"
        board += "1 2 3 4 5 6 7 "
        return board


class Player:
    def __init__(self, name, color):
        self.name, self.color = name, color

    def __str__(self):
        return self.name
