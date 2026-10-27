

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReadingAlarm(enum.StrEnum):
    STEADY = "steady"
    PULSED = "pulsed"

    def visit(self, steady: typing.Callable[[], T_Result], pulsed: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReadingAlarm.STEADY:
            return steady()
        if self is ReadingAlarm.PULSED:
            return pulsed()
