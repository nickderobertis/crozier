

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAlertsV2RequestPolicySeverity(enum.StrEnum):
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
        if self is GetAlertsV2RequestPolicySeverity.CRITICAL:
            return critical()
        if self is GetAlertsV2RequestPolicySeverity.HIGH:
            return high()
        if self is GetAlertsV2RequestPolicySeverity.MEDIUM:
            return medium()
        if self is GetAlertsV2RequestPolicySeverity.LOW:
            return low()
        if self is GetAlertsV2RequestPolicySeverity.INFORMATIONAL:
            return informational()
