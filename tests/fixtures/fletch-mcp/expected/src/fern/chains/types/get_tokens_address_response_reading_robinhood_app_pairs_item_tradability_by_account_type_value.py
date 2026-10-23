

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTokensAddressResponseReadingRobinhoodAppPairsItemTradabilityByAccountTypeValue(enum.StrEnum):
    TRADABLE = "tradable"
    UNTRADABLE = "untradable"

    def visit(self, tradable: typing.Callable[[], T_Result], untradable: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetTokensAddressResponseReadingRobinhoodAppPairsItemTradabilityByAccountTypeValue.TRADABLE:
            return tradable()
        if self is GetTokensAddressResponseReadingRobinhoodAppPairsItemTradabilityByAccountTypeValue.UNTRADABLE:
            return untradable()
