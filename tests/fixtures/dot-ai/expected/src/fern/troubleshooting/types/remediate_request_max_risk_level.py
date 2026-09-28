

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RemediateRequestMaxRiskLevel(enum.StrEnum):
    """
    For automatic mode: maximum risk level allowed for execution (default: low)
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
        if self is RemediateRequestMaxRiskLevel.LOW:
            return low()
        if self is RemediateRequestMaxRiskLevel.MEDIUM:
            return medium()
        if self is RemediateRequestMaxRiskLevel.HIGH:
            return high()
