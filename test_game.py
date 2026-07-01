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

