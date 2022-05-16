from tictactoe import Board, Player, Game
import pytest


class TestBoard:
    def test_display_empty(self):
        b = Board()
        assert (
            b.display()
            == " . | . | . \n-----------\n . | . | . \n-----------\n . | . | . "
        )

    def test_display_xs(self):

        b = Board()
        b.plays = ["X" for _ in range(9)]
        assert (
            b.display()
            == " X | X | X \n-----------\n X | X | X \n-----------\n X | X | X "
        )

    def test_display_os(self):
        b = Board()
        b.plays = ["O" for _ in range(9)]
        assert (
            b.display()
            == " O | O | O \n-----------\n O | O | O \n-----------\n O | O | O "
        )

    def test_available_empty(self):
        b = Board()
        assert (
            b.available_moves()
            == " 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 "
        )

    def test_available_full(self):
        b = Board()
        b.plays = ["O" if i % 2 else "X" for i in range(9)]
        assert (
            b.available_moves()
            == " X | O | X \n-----------\n O | X | O \n-----------\n X | O | X "
        )

    def test_available_partial(self):
        b = Board()
        b.plays = [
            "X" if i % 3 == 0 else "O" if i % 3 - 1 == 0 else "." for i in range(9)
        ]
        assert (
            b.available_moves()
            == " X | O | 3 \n-----------\n X | O | 6 \n-----------\n X | O | 9 "
        )

    def test_add_play(self):
        b = Board()
        b.add_play(1, "X")
        assert b.plays == ["X"] + ["."] * 8
        b.add_play(9, "O")
        assert b.plays == ["X"] + ["."] * 7 + ["O"]
        with pytest.raises(ValueError):
            b.add_play(9, "O")
            b.add_play(10, "X")


class TestPlayer:
    p = Player("Armando")

    def test_init(self):
        assert self.p.name == "Armando"
        assert self.p.wins == 0
        assert self.p.symbol == None


class TestGame:
    g = Game()

    def test_game(self):
        assert isinstance(self.g.board, Board)
        with pytest.raises(AttributeError):
            self.g.player_one.name
        assert self.g.turn == 0

    def test_add_player(self):
        self.g.add_player(Player("1")), self.g.add_player(Player("2"))
        with pytest.raises(ValueError):
            self.g.add_player(Player("3"))
        assert self.g.player_one.name == "1"
        assert self.g.player_one.symbol == "X"
        assert self.g.player_two.name == "2"
        assert self.g.player_two.symbol == "O"

    def test_check_no_winner(self):
        assert self.g.check_winner() == None
        for x in (1, 2, 5, 6, 7):
            self.g.board.add_play(x, "X")
            assert self.g.check_winner() == None

    def test_check_winner(self):
        self.g.board = Board()
        for x in (1, 2, 3):
            self.g.board.add_play(x, "X")
            print(self.g.board.display())
        assert self.g.check_winner() == self.g.player_one
        self.g.board = Board()
        for x in (3, 5, 7):
            self.g.board.add_play(x, "O")
        assert self.g.check_winner() == self.g.player_two

    def test_play_turn(self):
        self.g.board = Board()
        # play a game across the first 7 tiles in order, with players alternating
        # produces a win on turn 7
        for i in range(1, 7):
            self.g.play_turn(i)
            assert self.g.turn == i  # turn number happens to coincide with test plays
            assert self.g.board.plays[i - 1] == "O" if i % 2 == 0 else "X"
            assert self.g.check_winner() == None
        self.g.play_turn(7)
        assert self.g.check_winner() == self.g.player_one
        assert self.g.player_one.wins == 1
        with pytest.raises(ValueError):
            self.g.play_turn(1)
