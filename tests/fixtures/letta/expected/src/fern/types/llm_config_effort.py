

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LlmConfigEffort(enum.StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    def visit(
        self,
        low: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LlmConfigEffort.LOW:
            return low()
        if self is LlmConfigEffort.MEDIUM:
            return medium()
        if self is LlmConfigEffort.HIGH:
            return high()
