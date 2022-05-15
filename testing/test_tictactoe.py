from tictactoe import Board


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
