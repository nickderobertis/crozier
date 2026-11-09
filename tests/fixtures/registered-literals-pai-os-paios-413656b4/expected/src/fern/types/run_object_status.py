

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunObjectStatus(enum.StrEnum):
    """
    The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, or `expired`.
    """

    QUEUED = "queued"
    IN_PROGRESS = "in_progress"
    REQUIRES_ACTION = "requires_action"
    CANCELLING = "cancelling"
    CANCELLED = "cancelled"
    FAILED = "failed"
    COMPLETED = "completed"
    EXPIRED = "expired"

    def visit(
        self,
        queued: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        requires_action: typing.Callable[[], T_Result],
        cancelling: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunObjectStatus.QUEUED:
            return queued()
        if self is RunObjectStatus.IN_PROGRESS:
            return in_progress()
        if self is RunObjectStatus.REQUIRES_ACTION:
            return requires_action()
        if self is RunObjectStatus.CANCELLING:
            return cancelling()
        if self is RunObjectStatus.CANCELLED:
            return cancelled()
        if self is RunObjectStatus.FAILED:
            return failed()
        if self is RunObjectStatus.COMPLETED:
            return completed()
        if self is RunObjectStatus.EXPIRED:
            return expired()
