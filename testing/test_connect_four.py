import connect_four, pytest


@pytest.fixture
def new_board():
    return connect_four.Board()


class TestBoard:
    def test_init(self, new_board):
        assert isinstance(new_board, connect_four.Board)
        assert new_board.plays == {i: [] for i in range(7)}

    def test_add_play(self, new_board):
        # test filling a single row
        for i in range(7):
            color = connect_four.RED if i % 2 else connect_four.BLUE
            new_board.add_play(i, color)
            assert (
                new_board.plays[i][0] == color
            ), f"expected square at {i}, 0 to be {color}, instead it is {new_board.plays[i][0]}"

        # test plays outside of game bounds
        for i in [-1, 7]:
            with pytest.raises(ValueError) as e_out_of_bounds:
                new_board.add_play(i, connect_four.RED)
            assert "out of bounds" in str(
                e_out_of_bounds.value
            ), f"expected 'out of bounds' exception at column {i}"

        # test non-integer plays
        for i in ["red", True, "\033[92m"]:  # ]
            with pytest.raises(ValueError) as e_non_integer:
                new_board.add_play(i, connect_four.RED)
            assert "integer" in str(
                e_non_integer.value
            ), f"expected 'integer' exception for input {i}"

        # test plays with illegal colors
        for c in ["red", True, "\033[92m"]:  # ]
            with pytest.raises(ValueError) as e_color:
                new_board.add_play(0, c)
                assert "color" in str(
                    e_color.value
                ), f"expected 'invalid color exception for input {c}"
                assert (
                    len(new_board.plays[0]) == 1
                ), "invalid color should not change game board"

        # test filling the board
        for i in range(7 * 5):
            color = connect_four.RED if i % 2 else connect_four.BLUE
            new_board.add_play(i % 7, color)
            assert (
                new_board.plays[i % 7][(i // 7) + 1] == color
            ), f"expected square at {i % 7}, {(i // 7) + 1} to be {color}"

        # test playing filled columns
        for i in range(7):
            with pytest.raises(ValueError) as e_full_column:
                new_board.add_play(i, connect_four.RED)
            assert "full" in str(
                e_full_column.value
            ), f"expected 'full column' exception at column {i}"

    def test__str__(self, new_board):
        # visual testing only
        pass


@pytest.fixture
def player_one():
    return connect_four.Player("1", connect_four.RED)


@pytest.fixture
def player_two():
    return connect_four.Player("2", connect_four.BLUE)


class TestPlayer:
    def test_init(self, player_one, player_two):
        assert player_one.name == "1"
        assert player_one.color == connect_four.RED
        assert player_two.name == "2"
        assert player_two.color == connect_four.RED

    def test__str__(self, player_one, player_two):
        assert str(player_one) == "1"
        assert str(player_two) == "2"


@pytest.fixture
def new_game(player_one, player_two):
    return connect_four.Game(player_one, player_two)


class TestGame:
    def test_init(self):
        with pytest.raises(ValueError) as type_error:
            connect_four.Game(1, "2")
        assert "invalid type" in str(type_error.value)
        with pytest.raises(ValueError) as type_error:
            connect_four.Game("1", 2)
        assert "invalid type" in str(type_error.value)
        game = connect_four.Game("1", "2")
        assert isinstance(game.player_one, connect_four.Player)
        assert isinstance(game.player_two, connect_four.Player)
        assert game.player_one.color == connect_four.RED
        assert game.player_two.color == connect_four.BLUE
        assert game.board.plays == {i: [] for i in range(7)}
