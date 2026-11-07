

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CountdownBarInputScheduleType(enum.StrEnum):
    WEEKLY = "weekly"
    ONE_TIME = "one_time"

    def visit(self, weekly: typing.Callable[[], T_Result], one_time: typing.Callable[[], T_Result]) -> T_Result:
        if self is CountdownBarInputScheduleType.WEEKLY:
            return weekly()
        if self is CountdownBarInputScheduleType.ONE_TIME:
            return one_time()
