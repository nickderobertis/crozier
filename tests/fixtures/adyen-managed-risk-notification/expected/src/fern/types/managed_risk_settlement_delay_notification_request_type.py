

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ManagedRiskSettlementDelayNotificationRequestType(enum.StrEnum):
    """
    Type of webhook.
    """

    BALANCE_PLATFORM_MANAGED_RISK_SETTLEMENT_DELAY_UPDATED = "balancePlatform.managedRisk.settlementDelay.updated"

    def visit(self, balance_platform_managed_risk_settlement_delay_updated: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is ManagedRiskSettlementDelayNotificationRequestType.BALANCE_PLATFORM_MANAGED_RISK_SETTLEMENT_DELAY_UPDATED
        ):
            return balance_platform_managed_risk_settlement_delay_updated()
