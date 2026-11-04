

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionCallItemStatus(enum.StrEnum):
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    INCOMPLETE = "incomplete"

    def visit(
        self,
        in_progress: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        incomplete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FunctionCallItemStatus.IN_PROGRESS:
            return in_progress()
        if self is FunctionCallItemStatus.COMPLETED:
            return completed()
        if self is FunctionCallItemStatus.INCOMPLETE:
            return incomplete()
