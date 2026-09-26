

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PolicyModelSeverity(enum.StrEnum):
    """
    Severity
    """

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

    def visit(
        self,
        high: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PolicyModelSeverity.HIGH:
            return high()
        if self is PolicyModelSeverity.MEDIUM:
            return medium()
        if self is PolicyModelSeverity.LOW:
            return low()
