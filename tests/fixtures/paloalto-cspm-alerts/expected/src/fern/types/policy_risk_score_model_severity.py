

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PolicyRiskScoreModelSeverity(enum.StrEnum):
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
        if self is PolicyRiskScoreModelSeverity.HIGH:
            return high()
        if self is PolicyRiskScoreModelSeverity.MEDIUM:
            return medium()
        if self is PolicyRiskScoreModelSeverity.LOW:
            return low()
