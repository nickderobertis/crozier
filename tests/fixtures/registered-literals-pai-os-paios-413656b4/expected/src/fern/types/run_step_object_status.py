

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunStepObjectStatus(enum.StrEnum):
    """
    The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.
    """

    IN_PROGRESS = "in_progress"
    CANCELLED = "cancelled"
    FAILED = "failed"
    COMPLETED = "completed"
    EXPIRED = "expired"

    def visit(
        self,
        in_progress: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunStepObjectStatus.IN_PROGRESS:
            return in_progress()
        if self is RunStepObjectStatus.CANCELLED:
            return cancelled()
        if self is RunStepObjectStatus.FAILED:
            return failed()
        if self is RunStepObjectStatus.COMPLETED:
            return completed()
        if self is RunStepObjectStatus.EXPIRED:
            return expired()
