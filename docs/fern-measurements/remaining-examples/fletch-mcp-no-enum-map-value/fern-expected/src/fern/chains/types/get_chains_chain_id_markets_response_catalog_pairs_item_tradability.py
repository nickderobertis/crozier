

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdMarketsResponseCatalogPairsItemTradability(enum.StrEnum):
    TRADABLE = "tradable"
    UNTRADABLE = "untradable"

    def visit(self, tradable: typing.Callable[[], T_Result], untradable: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetChainsChainIdMarketsResponseCatalogPairsItemTradability.TRADABLE:
            return tradable()
        if self is GetChainsChainIdMarketsResponseCatalogPairsItemTradability.UNTRADABLE:
            return untradable()
