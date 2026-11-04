

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SubscribeToGameEventsResponseItemOneEvent(enum.StrEnum):
    PLAYER_JOIN = "playerJoin"

    def visit(self, player_join: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubscribeToGameEventsResponseItemOneEvent.PLAYER_JOIN:
            return player_join()
