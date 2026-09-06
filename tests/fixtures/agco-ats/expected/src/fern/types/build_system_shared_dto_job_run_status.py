

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BuildSystemSharedDtoJobRunStatus(enum.StrEnum):
    """
    The status of this JobRun
    """

    READY = "Ready"
    IN_PROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    CANCELLED = "Cancelled"
    FAILED = "Failed"

    def visit(
        self,
        ready: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BuildSystemSharedDtoJobRunStatus.READY:
            return ready()
        if self is BuildSystemSharedDtoJobRunStatus.IN_PROGRESS:
            return in_progress()
        if self is BuildSystemSharedDtoJobRunStatus.SUCCEEDED:
            return succeeded()
        if self is BuildSystemSharedDtoJobRunStatus.CANCELLED:
            return cancelled()
        if self is BuildSystemSharedDtoJobRunStatus.FAILED:
            return failed()
