

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AsyncJobStatus(enum.StrEnum):
    """
    Job status
    """

    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    READY_TO_DOWNLOAD = "READY_TO_DOWNLOAD"
    SUBMITTED = "SUBMITTED"

    def visit(
        self,
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        ready_to_download: typing.Callable[[], T_Result],
        submitted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AsyncJobStatus.COMPLETED:
            return completed()
        if self is AsyncJobStatus.FAILED:
            return failed()
        if self is AsyncJobStatus.IN_PROGRESS:
            return in_progress()
        if self is AsyncJobStatus.READY_TO_DOWNLOAD:
            return ready_to_download()
        if self is AsyncJobStatus.SUBMITTED:
            return submitted()
