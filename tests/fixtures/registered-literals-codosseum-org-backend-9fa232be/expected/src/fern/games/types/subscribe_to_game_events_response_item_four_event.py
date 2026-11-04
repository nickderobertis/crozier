

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SubscribeToGameEventsResponseItemFourEvent(enum.StrEnum):
    ROUND_OVER = "roundOver"

    def visit(self, round_over: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubscribeToGameEventsResponseItemFourEvent.ROUND_OVER:
            return round_over()
