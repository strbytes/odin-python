import connect_four, pytest


@pytest.fixture
def new_board():
    return connect_four.Board()


class TestBoard:
    def test_init(self, new_board):
        assert isinstance(new_board, connect_four.Board)
        assert new_board.plays == {i: ["" for _ in range(6)] for i in range(7)}

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
        assert player_two.color == connect_four.BLUE

    def test__str__(self, player_one, player_two):
        assert str(player_one) == "1"
        assert str(player_two) == "2"


@pytest.fixture
def new_game(player_one, player_two):
    return connect_four.Game(player_one, player_two)


@pytest.fixture
def game_win_states():
    def state_generator():
        four = range(4)
        for y in range(6):
            for x in range(7):
                color = connect_four.RED if (x + y) % 2 == 0 else connect_four.BLUE

                if x + 3 < 7:
                    b = connect_four.Board()
                    xs = [i + x for i in four]
                    for play_x in xs:
                        b.plays[play_x][y] = color
                    g = connect_four.Game()
                    g.board = b
                    yield g

                if y + 3 < 6:
                    b = connect_four.Board()
                    ys = [i + y for i in four]
                    for play_y in ys:
                        b.plays[x][play_y] = color
                    g = connect_four.Game()
                    g.board = b
                    yield g

                if x + 3 < 7 and y + 3 < 6:
                    b = connect_four.Board()
                    xs = [i + x for i in four]
                    ys = [i + y for i in four]
                    for i in four:
                        b.plays[xs[i]][ys[i]] = color
                    g = connect_four.Game()
                    g.board = b
                    yield g

    return state_generator()


def get_coords_from_win_state(game):
    coords = []
    for y in range(6):
        for x in range(7):
            if game.board.plays[x][y]:
                coords.append((x, y))
    return coords


@pytest.fixture
def game_no_win_states():
    def state_generator():
        four = range(4)
        no_win = [
            [connect_four.RED, connect_four.BLUE, connect_four.BLUE, connect_four.BLUE],
            [connect_four.BLUE, connect_four.RED, connect_four.BLUE, connect_four.BLUE],
            [connect_four.RED, connect_four.RED, connect_four.BLUE, connect_four.RED],
            [connect_four.RED, connect_four.RED, connect_four.RED, connect_four.BLUE],
        ]

        for y in range(6):
            for x in range(7):
                if x + 3 < 7 and y + 3 < 6:
                    b = connect_four.Board()
                    for x_play in four:
                        for y_play in four:
                            b.plays[x_play + x][y_play + y] = no_win[x_play][y_play]
                    g = connect_four.Game()
                    g.board = b
                    yield g

    return state_generator()


class TestGame:
    def test_init(self):
        with pytest.raises(ValueError) as type_error:
            connect_four.Game(1, "2")
        assert "invalid type" in str(
            type_error.value
        ), "expected 'invalid type' exception for input 2"
        with pytest.raises(ValueError) as type_error:
            connect_four.Game("1", 2)
        assert "invalid type" in str(
            type_error.value
        ), "expected 'invalid type' exception for input 1"
        game = connect_four.Game("1", "2")
        assert isinstance(
            game.player_one, connect_four.Player
        ), "expected game.player_one to be Player"
        assert isinstance(
            game.player_two, connect_four.Player
        ), "expected game.player_two to be Player"
        assert (
            game.player_one.color == connect_four.RED
        ), "expected game.player_one.color to be RED"
        assert (
            game.player_two.color == connect_four.BLUE
        ), "expected game.player_two.color to be BLUE"
        assert game.board.plays == {
            i: [] for i in range(7)
        }, "expected game board to be empty Board"

    def test_play_turn(self, new_game, capsys):
        new_game.play_turn(8)
        captured = capsys.readouterr()
        assert (
            "column from 1 to 7" in captured.out
        ), "expected message about incorrect play attempt for input 8"
        new_game.play_turn("a")
        captured = capsys.readouterr()
        assert (
            "column from 1 to 7" in captured.out
        ), "expected message about incorrect play attempt for input 'a'"
        for i in range(6):
            new_game.play_turn(1)
            turn = connect_four.RED if i % 2 == 0 else connect_four.BLUE
            assert (
                new_game.board.plays[0][i] == turn
            ), f"expected {turn} at new_game.board.plays[0][{i}]"
        new_game.play_turn(1)
        captured = capsys.readouterr()
        assert (
            "column is full" in captured.out
        ), "expected column is full exception for input 1"

