

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SubscribeToGameEventsResponseItemDataEvent(enum.StrEnum):
    GAME_OVER = "gameOver"

    def visit(self, game_over: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubscribeToGameEventsResponseItemDataEvent.GAME_OVER:
            return game_over()
