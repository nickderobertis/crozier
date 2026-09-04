

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ManagedRiskReserveWaiverRemovedNotificationRequestType(enum.StrEnum):
    """
    Type of webhook.
    """

    BALANCE_PLATFORM_MANAGED_RISK_RESERVE_WAIVER_REMOVED = "balancePlatform.managedRisk.reserveWaiver.removed"

    def visit(self, balance_platform_managed_risk_reserve_waiver_removed: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is ManagedRiskReserveWaiverRemovedNotificationRequestType.BALANCE_PLATFORM_MANAGED_RISK_RESERVE_WAIVER_REMOVED
        ):
            return balance_platform_managed_risk_reserve_waiver_removed()
