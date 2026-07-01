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

    def calc_game_score(self, guessNumber):

        result = False
        strike = 0
        ball = 0

        for idx, num in enumerate(self._question):
            for guess_idx, guess_num in enumerate(guessNumber):
                if num == guess_num:
                    if idx == guess_idx:
                        strike += 1
                    else:
                        ball += 1

        if strike == 3: result = True

        return result, strike, ball


    def guess(self, guessNumber) -> GameResult:
        self.assert_illigal_value(guessNumber)
        result, strike, ball = self.calc_game_score(guessNumber)
        return GameResult(result, strike, ball)

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