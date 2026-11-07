

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TextParamVerbosity(enum.StrEnum):
    """
    Controls the level of detail in generated text output.
    """

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    def visit(
        self,
        low: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TextParamVerbosity.LOW:
            return low()
        if self is TextParamVerbosity.MEDIUM:
            return medium()
        if self is TextParamVerbosity.HIGH:
            return high()
