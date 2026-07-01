from typing import Any, Optional

from game_result import GameResult


class Game:
    def __init__(self):
        self._question = ""

    @property
    def question(self):
        raise AttributeError("읽을 수 없음")

    @question.setter
    def question(self, value):
        self._question = value

    def guess(self, guessNumber) -> GameResult or None:
        self.assert_illigal_value(guessNumber)
        if guessNumber == self._question :
            return GameResult(True,3,0)
        return None

    def assert_illigal_value(self, guessNumber):
        if guessNumber is None:
            raise TypeError()

        if len(guessNumber) != 3:
            raise TypeError()

        if not guessNumber.isdigit():
            raise TypeError()

        if self.isDuplicatedNumber(guessNumber):
            raise TypeError()

    def isDuplicatedNumber(self, guessNumber) -> Any:
        return len(set(guessNumber)) != 3