

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAlertsRequestPolicySeverity(enum.StrEnum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFORMATIONAL = "informational"

    def visit(
        self,
        critical: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
        informational: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetAlertsRequestPolicySeverity.CRITICAL:
            return critical()
        if self is GetAlertsRequestPolicySeverity.HIGH:
            return high()
        if self is GetAlertsRequestPolicySeverity.MEDIUM:
            return medium()
        if self is GetAlertsRequestPolicySeverity.LOW:
            return low()
        if self is GetAlertsRequestPolicySeverity.INFORMATIONAL:
            return informational()
