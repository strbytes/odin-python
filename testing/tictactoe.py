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


def play_round(player_one, player_two):
    game = Game()
    game.add_player(player_one)
    game.add_player(player_two)
    winner = None
    while not winner:
        print()
        print(game.board.available_moves())
        play = input(str(game.whose_turn) + ", choose your play: ")
        try:
            game.play_turn(int(play))
        except ValueError as e:
            if e.args[0] == "square already played":
                print("That square has already been played.")
        winner = game.check_winner()
    print(game.board.display())
    print(str(winner) + " wins!")
    return winner


if __name__ == "__main__":
    player_one = Player(input("Player One, enter your name: "))
    player_two = Player(input("Player Two, enter your name: "))
    winner = play_round(player_one, player_two)
    if "y" in input("Two out of three?").lower():
        while player_one.wins < 2 and player_two.wins < 2:
            winner = play_round(player_one, player_two)
            print(
                f"The score is: \n{player_one}: {player_one.wins}\n"
                + f"{player_two}: {player_two.wins}"
            )
    print("Game over")
