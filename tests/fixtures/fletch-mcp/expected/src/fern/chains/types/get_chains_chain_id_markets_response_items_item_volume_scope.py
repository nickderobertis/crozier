

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdMarketsResponseItemsItemVolumeScope(enum.StrEnum):
    SELECTED_POOL = "selected_pool"

    def visit(self, selected_pool: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetChainsChainIdMarketsResponseItemsItemVolumeScope.SELECTED_POOL:
            return selected_pool()
