from tictactoe import Board
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
