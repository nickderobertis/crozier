

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SubscribeToGameEventsResponseItemSevenEvent(enum.StrEnum):
    PLAYER_FINISH = "playerFinish"

    def visit(self, player_finish: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubscribeToGameEventsResponseItemSevenEvent.PLAYER_FINISH:
            return player_finish()
