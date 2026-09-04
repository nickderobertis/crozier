

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduleRunStatus(enum.StrEnum):
    SCHEDULED = "scheduled"
    TRIGGERED = "triggered"
    FAILED = "failed"

    def visit(
        self,
        scheduled: typing.Callable[[], T_Result],
        triggered: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ScheduleRunStatus.SCHEDULED:
            return scheduled()
        if self is ScheduleRunStatus.TRIGGERED:
            return triggered()
        if self is ScheduleRunStatus.FAILED:
            return failed()
