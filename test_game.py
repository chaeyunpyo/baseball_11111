import pytest
from game import Game

@pytest.fixture
def game():
    return Game()

@pytest.mark.parametrize("value_input", [None, "12", "1234", "12s", "121"])
def test_exception_when_invalid_input(game, value_input):
    assert_illegal_argument(game, value_input)

def assert_matced_number(result, solved: bool, strikes: int, balls: int):
    assert result is not None
    assert result.solved == solved
    assert result.strikes == strikes
    assert result.balls == balls

def assert_illegal_argument(game: Game, guessnumbers: str):
    with pytest.raises(TypeError):
        game.guess(guessnumbers)

def test_return_solved_result_if_matched_number(game):
    game.question = "123"
    assert_matced_number(game.guess("123"), True, 3, 0)

def test_return_solved_result_if_unmatched_number(game):
    game.question = "123"
    assert_matced_number(game.guess("456"), False, 0, 0)

def test_return_solved_result_if_2strike_0ball_number(game):
    game.question = "123"
    assert_matced_number(game.guess("124"), False, 2, 0)

