

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateApprovalRequestRiskLevel(enum.StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    CRITICAL = "critical"

    def visit(
        self,
        low: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        critical: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateApprovalRequestRiskLevel.LOW:
            return low()
        if self is CreateApprovalRequestRiskLevel.MEDIUM:
            return medium()
        if self is CreateApprovalRequestRiskLevel.CRITICAL:
            return critical()
