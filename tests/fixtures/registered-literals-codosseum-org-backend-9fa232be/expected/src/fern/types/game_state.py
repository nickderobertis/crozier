

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GameState(enum.StrEnum):
    """
    The available game states
    """

    WARMUP = "warmup"
    IN_PROGRESS = "inProgress"
    ROUND_OVER = "roundOver"
    GAME_OVER = "gameOver"

    def visit(
        self,
        warmup: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        round_over: typing.Callable[[], T_Result],
        game_over: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GameState.WARMUP:
            return warmup()
        if self is GameState.IN_PROGRESS:
            return in_progress()
        if self is GameState.ROUND_OVER:
            return round_over()
        if self is GameState.GAME_OVER:
            return game_over()
