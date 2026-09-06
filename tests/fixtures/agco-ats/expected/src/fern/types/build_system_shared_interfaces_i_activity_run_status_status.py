

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BuildSystemSharedInterfacesIActivityRunStatusStatus(enum.StrEnum):
    """
    Gets or sets the status of the activity run.
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
        if self is BuildSystemSharedInterfacesIActivityRunStatusStatus.READY:
            return ready()
        if self is BuildSystemSharedInterfacesIActivityRunStatusStatus.IN_PROGRESS:
            return in_progress()
        if self is BuildSystemSharedInterfacesIActivityRunStatusStatus.SUCCEEDED:
            return succeeded()
        if self is BuildSystemSharedInterfacesIActivityRunStatusStatus.CANCELLED:
            return cancelled()
        if self is BuildSystemSharedInterfacesIActivityRunStatusStatus.FAILED:
            return failed()
