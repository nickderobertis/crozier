

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SubscribeToGameEventsResponseItemThreeEvent(enum.StrEnum):
    ROUND_START = "roundStart"

    def visit(self, round_start: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubscribeToGameEventsResponseItemThreeEvent.ROUND_START:
            return round_start()
