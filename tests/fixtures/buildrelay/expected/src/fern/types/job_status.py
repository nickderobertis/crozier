

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobStatus(enum.StrEnum):
    """
    Current job status
    """

    QUEUED = "Queued"
    RUNNING = "running"
    COMPLETE = "complete"
    FAILED = "failed"

    def visit(
        self,
        queued: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobStatus.QUEUED:
            return queued()
        if self is JobStatus.RUNNING:
            return running()
        if self is JobStatus.COMPLETE:
            return complete()
        if self is JobStatus.FAILED:
            return failed()
