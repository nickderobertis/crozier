

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ValidationTaskStatus(enum.StrEnum):
    READY = "ready"
    IN_PROGRESS = "in-progress"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"

    def visit(
        self,
        ready: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ValidationTaskStatus.READY:
            return ready()
        if self is ValidationTaskStatus.IN_PROGRESS:
            return in_progress()
        if self is ValidationTaskStatus.SUCCEEDED:
            return succeeded()
        if self is ValidationTaskStatus.FAILED:
            return failed()
        if self is ValidationTaskStatus.CANCELLED:
            return cancelled()
