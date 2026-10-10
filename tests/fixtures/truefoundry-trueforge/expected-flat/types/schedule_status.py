

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduleStatus(enum.StrEnum):
    ACTIVE = "active"
    PAUSED = "paused"

    def visit(self, active: typing.Callable[[], T_Result], paused: typing.Callable[[], T_Result]) -> T_Result:
        if self is ScheduleStatus.ACTIVE:
            return active()
        if self is ScheduleStatus.PAUSED:
            return paused()
