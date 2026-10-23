

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TokenMarketRobinhoodAppPairsItemTradabilityByAccountTypeValue(enum.StrEnum):
    TRADABLE = "tradable"
    UNTRADABLE = "untradable"

    def visit(self, tradable: typing.Callable[[], T_Result], untradable: typing.Callable[[], T_Result]) -> T_Result:
        if self is TokenMarketRobinhoodAppPairsItemTradabilityByAccountTypeValue.TRADABLE:
            return tradable()
        if self is TokenMarketRobinhoodAppPairsItemTradabilityByAccountTypeValue.UNTRADABLE:
            return untradable()
