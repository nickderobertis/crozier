

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageObjectStatus(enum.StrEnum):
    """
    The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.
    """

    IN_PROGRESS = "in_progress"
    INCOMPLETE = "incomplete"
    COMPLETED = "completed"

    def visit(
        self,
        in_progress: typing.Callable[[], T_Result],
        incomplete: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MessageObjectStatus.IN_PROGRESS:
            return in_progress()
        if self is MessageObjectStatus.INCOMPLETE:
            return incomplete()
        if self is MessageObjectStatus.COMPLETED:
            return completed()
