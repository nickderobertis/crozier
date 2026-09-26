

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAlertsGroupedRequestPolicySeverity(enum.StrEnum):
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
        if self is GetAlertsGroupedRequestPolicySeverity.CRITICAL:
            return critical()
        if self is GetAlertsGroupedRequestPolicySeverity.HIGH:
            return high()
        if self is GetAlertsGroupedRequestPolicySeverity.MEDIUM:
            return medium()
        if self is GetAlertsGroupedRequestPolicySeverity.LOW:
            return low()
        if self is GetAlertsGroupedRequestPolicySeverity.INFORMATIONAL:
            return informational()
