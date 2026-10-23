

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServiceUnavailableErrorBodyItemsItemPairsItemTradability(enum.StrEnum):
    TRADABLE = "tradable"
    UNTRADABLE = "untradable"

    def visit(self, tradable: typing.Callable[[], T_Result], untradable: typing.Callable[[], T_Result]) -> T_Result:
        if self is ServiceUnavailableErrorBodyItemsItemPairsItemTradability.TRADABLE:
            return tradable()
        if self is ServiceUnavailableErrorBodyItemsItemPairsItemTradability.UNTRADABLE:
            return untradable()
