

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ActivityRunsGetActivityRunsRequestStatus(enum.StrEnum):
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
        if self is ActivityRunsGetActivityRunsRequestStatus.READY:
            return ready()
        if self is ActivityRunsGetActivityRunsRequestStatus.IN_PROGRESS:
            return in_progress()
        if self is ActivityRunsGetActivityRunsRequestStatus.SUCCEEDED:
            return succeeded()
        if self is ActivityRunsGetActivityRunsRequestStatus.CANCELLED:
            return cancelled()
        if self is ActivityRunsGetActivityRunsRequestStatus.FAILED:
            return failed()
