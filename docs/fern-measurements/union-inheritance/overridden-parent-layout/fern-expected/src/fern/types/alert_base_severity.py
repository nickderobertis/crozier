

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlertBaseSeverity(enum.StrEnum):
    """
    How urgent the alert is.
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
        if self is AlertBaseSeverity.LOW:
            return low()
        if self is AlertBaseSeverity.MEDIUM:
            return medium()
        if self is AlertBaseSeverity.HIGH:
            return high()
