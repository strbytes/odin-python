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


class Player:
    """Stores information about a player"""

    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.symbol = None

    def __str__(self):
        return self.name


class Game:
    """Stores the current game state"""

    def __init__(self):
        self.board = Board()
        self.player_one, self.player_two = None, None
        self.turn = 0

    @property
    def whose_turn(self):
        return self.player_one if self.turn % 2 == 0 else self.player_two

    def add_player(self, player):
        assert isinstance(player, Player), "Game requires a Player instance"
        if self.player_one is None:
            self.player_one = player
            self.player_one.symbol = "X"
        elif self.player_two is None:
            self.player_two = player
            self.player_two.symbol = "O"
        else:
            raise ValueError("Game only supports two players")

    def check_winner(self):
        win_states = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        p = self.board.plays
        for a, b, c in win_states:
            if p[a] == p[b] == p[c] != ".":
                return self.player_one if p[a] == "X" else self.player_two
        return None

    def play_turn(self, pos):
        self.board.add_play(pos, self.whose_turn.symbol)
        self.turn += 1
        if winner := self.check_winner():
            winner.wins += 1
            return winner
