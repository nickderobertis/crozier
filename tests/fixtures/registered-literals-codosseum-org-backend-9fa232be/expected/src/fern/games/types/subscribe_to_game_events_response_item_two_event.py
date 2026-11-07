

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SubscribeToGameEventsResponseItemTwoEvent(enum.StrEnum):
    PLAYER_LEAVE = "playerLeave"

    def visit(self, player_leave: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubscribeToGameEventsResponseItemTwoEvent.PLAYER_LEAVE:
            return player_leave()
