from tictactoe import Board, Player, Game
import pytest


@pytest.fixture
def new_board():
    return Board()


class TestBoard:
    def test_display_empty(self, new_board):
        assert (
            new_board.display()
            == " . | . | . \n-----------\n . | . | . \n-----------\n . | . | . "
        )

    def test_display_xs(self, new_board):
        new_board.plays = ["X" for _ in range(9)]
        assert (
            new_board.display()
            == " X | X | X \n-----------\n X | X | X \n-----------\n X | X | X "
        )

    def test_display_os(self, new_board):
        new_board.plays = ["O" for _ in range(9)]
        assert (
            new_board.display()
            == " O | O | O \n-----------\n O | O | O \n-----------\n O | O | O "
        )

    def test_available_empty(self, new_board):
        assert (
            new_board.available_moves()
            == " 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 "
        )

    def test_available_full(self, new_board):
        new_board.plays = ["O" if i % 2 else "X" for i in range(9)]
        assert (
            new_board.available_moves()
            == " X | O | X \n-----------\n O | X | O \n-----------\n X | O | X "
        )

    def test_available_partial(self, new_board):
        new_board.plays = [
            "X" if i % 3 == 0 else "O" if i % 3 - 1 == 0 else "." for i in range(9)
        ]
        assert (
            new_board.available_moves()
            == " X | O | 3 \n-----------\n X | O | 6 \n-----------\n X | O | 9 "
        )

    def test_add_play(self, new_board):
        new_board.add_play(1, "X")
        assert new_board.plays == ["X"] + ["."] * 8
        new_board.add_play(9, "O")
        assert new_board.plays == ["X"] + ["."] * 7 + ["O"]
        with pytest.raises(ValueError):
            new_board.add_play(9, "O")
            new_board.add_play(10, "X")


@pytest.fixture
def player_one():
    return Player("1")


@pytest.fixture
def player_two():
    return Player("2")


class TestPlayer:
    def test_init(self, player_one, player_two):
        assert player_one.name == "1"
        assert player_one.wins == 0
        assert player_one.symbol == None
        assert player_two.name == "2"
        assert player_two.wins == 0
        assert player_two.symbol == None


@pytest.fixture
def new_game():
    return Game()


@pytest.fixture
def game_with_players(new_game, player_one, player_two):
    new_game.add_player(player_one)
    new_game.add_player(player_two)
    return new_game


class TestGame:
    def test_game(self, new_game):
        assert isinstance(new_game.board, Board)
        with pytest.raises(AttributeError):
            new_game.player_one.name
        assert new_game.turn == 0

    def test_add_player(self, new_game, player_one, player_two):
        new_game.add_player(player_one),
        new_game.add_player(player_two)
        with pytest.raises(ValueError):
            new_game.add_player(player_one)
        assert new_game.player_one.name == "1"
        assert new_game.player_one.symbol == "X"
        assert new_game.player_two.name == "2"
        assert new_game.player_two.symbol == "O"

    def test_check_no_winner(self, new_game):
        assert new_game.check_winner() == None
        for x in (1, 2, 5, 6, 7):
            new_game.board.add_play(x, "X")
            assert new_game.check_winner() == None

    def test_check_winner(self, game_with_players):
        game_with_players.board = Board()
        for x in (1, 2, 3):
            game_with_players.board.add_play(x, "X")
        assert game_with_players.check_winner() == game_with_players.player_one
        game_with_players.board = Board()
        for x in (3, 5, 7):
            game_with_players.board.add_play(x, "O")
        assert game_with_players.check_winner() == game_with_players.player_two

    def test_play_turn(self, game_with_players):
        game_with_players.board = Board()
        # play a game across the first 7 tiles in order, with players alternating
        # produces a win on turn 7
        for i in range(1, 7):
            game_with_players.play_turn(i)
            assert (
                game_with_players.turn == i
            )  # turn number happens to coincide with test plays
            assert game_with_players.board.plays[i - 1] == "O" if i % 2 == 0 else "X"
            assert game_with_players.check_winner() == None
        game_with_players.play_turn(7)
        assert game_with_players.check_winner() == game_with_players.player_one
        assert game_with_players.player_one.wins == 1
        with pytest.raises(ValueError):
            game_with_players.play_turn(1)
