

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ToolApprovalDetailRiskLevel(enum.StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    CRITICAL = "critical"

    def visit(
        self,
        low: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        critical: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ToolApprovalDetailRiskLevel.LOW:
            return low()
        if self is ToolApprovalDetailRiskLevel.MEDIUM:
            return medium()
        if self is ToolApprovalDetailRiskLevel.CRITICAL:
            return critical()
