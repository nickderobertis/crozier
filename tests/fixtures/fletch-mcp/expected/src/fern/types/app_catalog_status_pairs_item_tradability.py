

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AppCatalogStatusPairsItemTradability(enum.StrEnum):
    TRADABLE = "tradable"
    UNTRADABLE = "untradable"

    def visit(self, tradable: typing.Callable[[], T_Result], untradable: typing.Callable[[], T_Result]) -> T_Result:
        if self is AppCatalogStatusPairsItemTradability.TRADABLE:
            return tradable()
        if self is AppCatalogStatusPairsItemTradability.UNTRADABLE:
            return untradable()
