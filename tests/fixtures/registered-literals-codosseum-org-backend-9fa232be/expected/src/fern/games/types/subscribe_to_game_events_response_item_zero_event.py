

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SubscribeToGameEventsResponseItemZeroEvent(enum.StrEnum):
    GAME_UPDATE = "gameUpdate"

    def visit(self, game_update: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubscribeToGameEventsResponseItemZeroEvent.GAME_UPDATE:
            return game_update()
