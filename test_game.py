import pytest
from game import Game

@pytest.fixture
def game():
    return Game()

@pytest.mark.parametrize("value_input", [None, "12", "1234", "12s", "121"])
def test_exception_when_invalid_input(game, value_input):
    assert_illegal_argument(game, value_input)

def assert_illegal_argument(game: Game, guessnumbers: str):
    with pytest.raises(TypeError):
        game.guess(guessnumbers)

def test_return_solved_result_if_matched_number(game):
    game.question = "123"
    result = game.guess("123")

    assert result is not None
    assert result.solved == True
    assert result.strikes == 3
    assert result.balls == 0

def test_return_solved_result_if_unmatched_number(game):
    game.question = "123"
    result = game.guess("456")

    assert result is not None
    assert result.solved == False
    assert result.strikes == 0
    assert result.balls == 0

