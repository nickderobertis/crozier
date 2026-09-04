

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ManagedRiskRollingReserveUpdatedNotificationRequestType(enum.StrEnum):
    """
    Type of webhook.
    """

    BALANCE_PLATFORM_MANAGED_RISK_ROLLING_RESERVE_UPDATED = "balancePlatform.managedRisk.rollingReserve.updated"

    def visit(self, balance_platform_managed_risk_rolling_reserve_updated: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is ManagedRiskRollingReserveUpdatedNotificationRequestType.BALANCE_PLATFORM_MANAGED_RISK_ROLLING_RESERVE_UPDATED
        ):
            return balance_platform_managed_risk_rolling_reserve_updated()
