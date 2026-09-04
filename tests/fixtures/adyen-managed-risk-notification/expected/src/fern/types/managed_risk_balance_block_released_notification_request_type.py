

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ManagedRiskBalanceBlockReleasedNotificationRequestType(enum.StrEnum):
    """
    Type of webhook.
    """

    BALANCE_PLATFORM_MANAGED_RISK_BALANCE_BLOCK_RELEASED = "balancePlatform.managedRisk.balance.block.released"

    def visit(self, balance_platform_managed_risk_balance_block_released: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is ManagedRiskBalanceBlockReleasedNotificationRequestType.BALANCE_PLATFORM_MANAGED_RISK_BALANCE_BLOCK_RELEASED
        ):
            return balance_platform_managed_risk_balance_block_released()
