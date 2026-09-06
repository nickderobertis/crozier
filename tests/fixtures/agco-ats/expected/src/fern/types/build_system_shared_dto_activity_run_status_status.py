

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BuildSystemSharedDtoActivityRunStatusStatus(enum.StrEnum):
    """
    The status of the ActivityRun
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
        if self is BuildSystemSharedDtoActivityRunStatusStatus.READY:
            return ready()
        if self is BuildSystemSharedDtoActivityRunStatusStatus.IN_PROGRESS:
            return in_progress()
        if self is BuildSystemSharedDtoActivityRunStatusStatus.SUCCEEDED:
            return succeeded()
        if self is BuildSystemSharedDtoActivityRunStatusStatus.CANCELLED:
            return cancelled()
        if self is BuildSystemSharedDtoActivityRunStatusStatus.FAILED:
            return failed()
