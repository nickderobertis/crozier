

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StepFeedback(enum.StrEnum):
    POSITIVE = "positive"
    NEGATIVE = "negative"

    def visit(self, positive: typing.Callable[[], T_Result], negative: typing.Callable[[], T_Result]) -> T_Result:
        if self is StepFeedback.POSITIVE:
            return positive()
        if self is StepFeedback.NEGATIVE:
            return negative()
