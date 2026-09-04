

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ManagedRiskRollingReserveLiftedNotificationRequestType(enum.StrEnum):
    """
    Type of webhook.
    """

    BALANCE_PLATFORM_MANAGED_RISK_ROLLING_RESERVE_LIFTED = "balancePlatform.managedRisk.rollingReserve.lifted"

    def visit(self, balance_platform_managed_risk_rolling_reserve_lifted: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is ManagedRiskRollingReserveLiftedNotificationRequestType.BALANCE_PLATFORM_MANAGED_RISK_ROLLING_RESERVE_LIFTED
        ):
            return balance_platform_managed_risk_rolling_reserve_lifted()
