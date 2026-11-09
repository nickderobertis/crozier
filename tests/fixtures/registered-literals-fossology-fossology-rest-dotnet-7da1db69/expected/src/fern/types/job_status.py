

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobStatus(enum.StrEnum):
    """
    Denotes the current status of the job in the queue
    """

    COMPLETED = "Completed"
    FAILED = "Failed"
    QUEUED = "Queued"
    PROCESSING = "Processing"

    def visit(
        self,
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        queued: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobStatus.COMPLETED:
            return completed()
        if self is JobStatus.FAILED:
            return failed()
        if self is JobStatus.QUEUED:
            return queued()
        if self is JobStatus.PROCESSING:
            return processing()
