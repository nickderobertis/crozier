

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DailyOpsRunStatus(enum.StrEnum):
    SCHEDULED = "scheduled"
    RUNNING = "running"
    COMPLETED = "completed"
    EMPTY = "empty"
    FAILED = "failed"
    BLOCKED = "blocked"

    def visit(
        self,
        scheduled: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        empty: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DailyOpsRunStatus.SCHEDULED:
            return scheduled()
        if self is DailyOpsRunStatus.RUNNING:
            return running()
        if self is DailyOpsRunStatus.COMPLETED:
            return completed()
        if self is DailyOpsRunStatus.EMPTY:
            return empty()
        if self is DailyOpsRunStatus.FAILED:
            return failed()
        if self is DailyOpsRunStatus.BLOCKED:
            return blocked()
