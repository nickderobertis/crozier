

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionCallItemParamStatus(enum.StrEnum):
    """
    The status of the function tool call.
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
        if self is FunctionCallItemParamStatus.IN_PROGRESS:
            return in_progress()
        if self is FunctionCallItemParamStatus.COMPLETED:
            return completed()
        if self is FunctionCallItemParamStatus.INCOMPLETE:
            return incomplete()
