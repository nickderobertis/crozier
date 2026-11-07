

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionCallOutputItemParamStatus(enum.StrEnum):
    """
    The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.
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
        if self is FunctionCallOutputItemParamStatus.IN_PROGRESS:
            return in_progress()
        if self is FunctionCallOutputItemParamStatus.COMPLETED:
            return completed()
        if self is FunctionCallOutputItemParamStatus.INCOMPLETE:
            return incomplete()
