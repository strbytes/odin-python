class Board:
    def __init__(self):
        self.plays = ["." for _ in range(9)]

    def add_play(self, pos, symbol):
        if len(symbol) != 1:
            raise ValueError("Board only accepts single character symbols")
        if (pos - 1) not in range(len(self.plays)):
            raise IndexError("Board only accepts plays in positions 0 - 9")
        if self.plays[pos - 1] != ".":
            raise ValueError("square already played")
        # positions displayed to the user are 1-indexed
        self.plays[pos - 1] = symbol

    def display(self):
        return (
            f" {self.plays[0]} | {self.plays[1]} | {self.plays[2]} \n"
            + "-----------\n"
            + f" {self.plays[3]} | {self.plays[4]} | {self.plays[5]} \n"
            + "-----------\n"
            + f" {self.plays[6]} | {self.plays[7]} | {self.plays[8]} "
        )

    def available_moves(self):
        available = [i + 1 if self.plays[i] == "." else self.plays[i] for i in range(9)]
        return (
            f" {available[0]} | {available[1]} | {available[2]} \n"
            + "-----------\n"
            + f" {available[3]} | {available[4]} | {available[5]} \n"
            + "-----------\n"
            + f" {available[6]} | {available[7]} | {available[8]} "
        )
