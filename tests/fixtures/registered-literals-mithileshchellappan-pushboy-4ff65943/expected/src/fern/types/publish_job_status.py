

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PublishJobStatus(enum.StrEnum):
    QUEUED = "QUEUED"
    SCHEDULED = "SCHEDULED"
    IN_PROGRESS = "IN_PROGRESS"
    DISPATCHED = "DISPATCHED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

    def visit(
        self,
        queued: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        dispatched: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PublishJobStatus.QUEUED:
            return queued()
        if self is PublishJobStatus.SCHEDULED:
            return scheduled()
        if self is PublishJobStatus.IN_PROGRESS:
            return in_progress()
        if self is PublishJobStatus.DISPATCHED:
            return dispatched()
        if self is PublishJobStatus.COMPLETED:
            return completed()
        if self is PublishJobStatus.FAILED:
            return failed()
