from typing import Any, Optional

from game_result import GameResult


class Game:
    def guess(self, guessNumber) -> GameResult:
        self.assert_illigal_value(guessNumber)
        return GameResult(True,3,0)

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