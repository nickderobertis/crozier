

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionCallOutputStatus(enum.StrEnum):
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
        if self is FunctionCallOutputStatus.IN_PROGRESS:
            return in_progress()
        if self is FunctionCallOutputStatus.COMPLETED:
            return completed()
        if self is FunctionCallOutputStatus.INCOMPLETE:
            return incomplete()
