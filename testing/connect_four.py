RED = "\x1b[91m"
BLUE = "\x1b[94m"
GREEN = "\x1b[92m"
ENDC = "\x1b[0m"
# ]]]] Treesitter thinks the brackets in the quotes are code and is indenting based on them -_-;


class Board:
    def __init__(self):
        self.plays = {i: ["" for _ in range(6)] for i in range(7)}

    def add_play(self, column, color):
        if type(column) is not int:
            raise TypeError(f"add_play accepts integers as input, not {type(column)}")
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

    def add_win(self, coords):
        for x, y in coords:
            self.plays[x][y] = GREEN

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


class Game:
    def __init__(self, p1_name="Player 1", p2_name="Player 2"):
        if not type(p1_name) == str:
            raise TypeError("invalid type for p1_name: expected string")
        if not type(p2_name) == str:
            raise TypeError("invalid type for p2_name, expected string")
        self.board = Board()
        self.player_one, self.player_two = Player(p1_name, RED), Player(p2_name, BLUE)
        self.turn = 0

    @property
    def whose_turn(self):
        return self.player_one if self.turn % 2 == 0 else self.player_two

    def play_turn(self, column):
        if type(column) is not int:
            raise TypeError(f"play_turn only accepts integers, not {type(column)}")
        self.board.add_play(column - 1, self.whose_turn.color)
        self.turn += 1
