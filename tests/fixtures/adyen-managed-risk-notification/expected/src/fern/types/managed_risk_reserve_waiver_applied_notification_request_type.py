

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ManagedRiskReserveWaiverAppliedNotificationRequestType(enum.StrEnum):
    """
    Type of webhook.
    """

    BALANCE_PLATFORM_MANAGED_RISK_RESERVE_WAIVER_APPLIED = "balancePlatform.managedRisk.reserveWaiver.applied"

    def visit(self, balance_platform_managed_risk_reserve_waiver_applied: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is ManagedRiskReserveWaiverAppliedNotificationRequestType.BALANCE_PLATFORM_MANAGED_RISK_RESERVE_WAIVER_APPLIED
        ):
            return balance_platform_managed_risk_reserve_waiver_applied()
