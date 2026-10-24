

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProposalRisk(enum.StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

    def visit(
        self,
        low: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        critical: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProposalRisk.LOW:
            return low()
        if self is ProposalRisk.MEDIUM:
            return medium()
        if self is ProposalRisk.HIGH:
            return high()
        if self is ProposalRisk.CRITICAL:
            return critical()
