

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdDexPoolsRequestSort(enum.StrEnum):
    TRACTION = "traction"
    DEPTH = "depth"
    VOLUME = "volume"
    SWAPS = "swaps"
    NEWEST = "newest"

    def visit(
        self,
        traction: typing.Callable[[], T_Result],
        depth: typing.Callable[[], T_Result],
        volume: typing.Callable[[], T_Result],
        swaps: typing.Callable[[], T_Result],
        newest: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdDexPoolsRequestSort.TRACTION:
            return traction()
        if self is GetChainsChainIdDexPoolsRequestSort.DEPTH:
            return depth()
        if self is GetChainsChainIdDexPoolsRequestSort.VOLUME:
            return volume()
        if self is GetChainsChainIdDexPoolsRequestSort.SWAPS:
            return swaps()
        if self is GetChainsChainIdDexPoolsRequestSort.NEWEST:
            return newest()
