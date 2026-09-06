

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BuildSystemSharedInterfacesIJobRunStatus(enum.StrEnum):
    """
    status
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
        if self is BuildSystemSharedInterfacesIJobRunStatus.READY:
            return ready()
        if self is BuildSystemSharedInterfacesIJobRunStatus.IN_PROGRESS:
            return in_progress()
        if self is BuildSystemSharedInterfacesIJobRunStatus.SUCCEEDED:
            return succeeded()
        if self is BuildSystemSharedInterfacesIJobRunStatus.CANCELLED:
            return cancelled()
        if self is BuildSystemSharedInterfacesIJobRunStatus.FAILED:
            return failed()
