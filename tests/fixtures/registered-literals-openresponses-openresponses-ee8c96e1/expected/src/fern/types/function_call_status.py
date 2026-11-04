

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionCallStatus(enum.StrEnum):
    """
    The status of the function call item that was recorded.
    """

    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    INCOMPLETE = "incomplete"

    def visit(
        self,
        in_progress: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        incomplete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FunctionCallStatus.IN_PROGRESS:
            return in_progress()
        if self is FunctionCallStatus.COMPLETED:
            return completed()
        if self is FunctionCallStatus.INCOMPLETE:
            return incomplete()
