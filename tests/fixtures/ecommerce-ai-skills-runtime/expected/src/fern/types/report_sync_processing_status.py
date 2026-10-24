

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReportSyncProcessingStatus(enum.StrEnum):
    IN_QUEUE = "IN_QUEUE"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    CANCELLED = "CANCELLED"
    FATAL = "FATAL"

    def visit(
        self,
        in_queue: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        done: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        fatal: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReportSyncProcessingStatus.IN_QUEUE:
            return in_queue()
        if self is ReportSyncProcessingStatus.IN_PROGRESS:
            return in_progress()
        if self is ReportSyncProcessingStatus.DONE:
            return done()
        if self is ReportSyncProcessingStatus.CANCELLED:
            return cancelled()
        if self is ReportSyncProcessingStatus.FATAL:
            return fatal()
