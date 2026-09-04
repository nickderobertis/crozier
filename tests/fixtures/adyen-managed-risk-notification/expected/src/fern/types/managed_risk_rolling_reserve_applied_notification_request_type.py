

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ManagedRiskRollingReserveAppliedNotificationRequestType(enum.StrEnum):
    """
    Type of webhook.
    """

    BALANCE_PLATFORM_MANAGED_RISK_ROLLING_RESERVE_APPLIED = "balancePlatform.managedRisk.rollingReserve.applied"

    def visit(self, balance_platform_managed_risk_rolling_reserve_applied: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is ManagedRiskRollingReserveAppliedNotificationRequestType.BALANCE_PLATFORM_MANAGED_RISK_ROLLING_RESERVE_APPLIED
        ):
            return balance_platform_managed_risk_rolling_reserve_applied()
