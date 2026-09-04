

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ManagedRiskSettlementDelayLiftedNotificationRequestType(enum.StrEnum):
    """
    Type of webhook.
    """

    BALANCE_PLATFORM_MANAGED_RISK_SETTLEMENT_DELAY_LIFTED = "balancePlatform.managedRisk.settlementDelay.lifted"

    def visit(self, balance_platform_managed_risk_settlement_delay_lifted: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is ManagedRiskSettlementDelayLiftedNotificationRequestType.BALANCE_PLATFORM_MANAGED_RISK_SETTLEMENT_DELAY_LIFTED
        ):
            return balance_platform_managed_risk_settlement_delay_lifted()
