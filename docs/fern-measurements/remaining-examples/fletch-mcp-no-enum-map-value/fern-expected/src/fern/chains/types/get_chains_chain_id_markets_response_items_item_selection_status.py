

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdMarketsResponseItemsItemSelectionStatus(enum.StrEnum):
    CURRENT = "current"
    STALE = "stale"
    MISSING = "missing"
    INVALID = "invalid"

    def visit(
        self,
        current: typing.Callable[[], T_Result],
        stale: typing.Callable[[], T_Result],
        missing: typing.Callable[[], T_Result],
        invalid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdMarketsResponseItemsItemSelectionStatus.CURRENT:
            return current()
        if self is GetChainsChainIdMarketsResponseItemsItemSelectionStatus.STALE:
            return stale()
        if self is GetChainsChainIdMarketsResponseItemsItemSelectionStatus.MISSING:
            return missing()
        if self is GetChainsChainIdMarketsResponseItemsItemSelectionStatus.INVALID:
            return invalid()
