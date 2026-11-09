

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SummarizationRequestBodySummarizationEffort(enum.StrEnum):
    LOW = "low"
    MEDIUM = "medium"

    def visit(self, low: typing.Callable[[], T_Result], medium: typing.Callable[[], T_Result]) -> T_Result:
        if self is SummarizationRequestBodySummarizationEffort.LOW:
            return low()
        if self is SummarizationRequestBodySummarizationEffort.MEDIUM:
            return medium()
