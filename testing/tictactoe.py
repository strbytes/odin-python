class Board:
    """Maintains the current game state of a tic-tac-toe board. Updates and
    displays the board when requested."""

    def __init__(self):
        self.plays = ["." for _ in range(9)]

    def add_play(self, pos, symbol):
        """Add a user play to self.plays. Note that user plays are 1-indexed
        and must be adjusted to work with self.plays"""
        if len(symbol) != 1:
            raise ValueError("Board only accepts single character symbols")
        if (pos - 1) not in range(len(self.plays)):
            raise IndexError("Board only accepts plays in positions 0 - 9")
        if self.plays[pos - 1] != ".":
            raise ValueError("square already played")
        self.plays[pos - 1] = symbol

    def display(self):
        """Return a string depiction of the state of the board"""
        return (
            f" {self.plays[0]} | {self.plays[1]} | {self.plays[2]} \n"
            + "-----------\n"
            + f" {self.plays[3]} | {self.plays[4]} | {self.plays[5]} \n"
            + "-----------\n"
            + f" {self.plays[6]} | {self.plays[7]} | {self.plays[8]} "
        )

    def available_moves(self):
        """Return a string depiction of the state of the board with numbers
        indicating squares available to be played"""
        available = [i + 1 if self.plays[i] == "." else self.plays[i] for i in range(9)]
        return (
            f" {available[0]} | {available[1]} | {available[2]} \n"
            + "-----------\n"
            + f" {available[3]} | {available[4]} | {available[5]} \n"
            + "-----------\n"
            + f" {available[6]} | {available[7]} | {available[8]} "
        )
