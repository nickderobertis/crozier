

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionCallOutputStatusEnum(enum.StrEnum):
    """
    Similar to `FunctionCallStatus`. All three options are allowed here for compatibility, but because in practice these items will be provided by developers, only `completed` should be used.
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
        if self is FunctionCallOutputStatusEnum.IN_PROGRESS:
            return in_progress()
        if self is FunctionCallOutputStatusEnum.COMPLETED:
            return completed()
        if self is FunctionCallOutputStatusEnum.INCOMPLETE:
            return incomplete()
