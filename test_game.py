import pytest
from game import Game

@pytest.fixture
def game():
    return Game()

def test_exception_when_invalid_input(game):
    assert_illegal_argument(game, None)
    assert_illegal_argument(game, "12")
    assert_illegal_argument(game, "1234")
    assert_illegal_argument(game, "12s")
    assert_illegal_argument(game, "121")



def assert_illegal_argument(game: Game, guessnumbers: str):
    try:
        game.guess(guessnumbers)
        pytest.fail()
    except TypeError:
        pass

