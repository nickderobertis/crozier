

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LineageActivityStatus(enum.StrEnum):
    SCHEDULED = "scheduled"
    STARTED = "started"
    ENDED = "ended"
    FAILED = "failed"
    CANCELLED = "cancelled"

    def visit(
        self,
        scheduled: typing.Callable[[], T_Result],
        started: typing.Callable[[], T_Result],
        ended: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LineageActivityStatus.SCHEDULED:
            return scheduled()
        if self is LineageActivityStatus.STARTED:
            return started()
        if self is LineageActivityStatus.ENDED:
            return ended()
        if self is LineageActivityStatus.FAILED:
            return failed()
        if self is LineageActivityStatus.CANCELLED:
            return cancelled()
