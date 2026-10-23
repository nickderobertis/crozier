

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdMarketsRequestSort(enum.StrEnum):
    VOLUME = "volume"
    SWAPS = "swaps"
    MARKET_CAP = "market_cap"
    V3DEPTH = "v3_depth"
    V4DEPTH = "v4_depth"
    NAME = "name"

    def visit(
        self,
        volume: typing.Callable[[], T_Result],
        swaps: typing.Callable[[], T_Result],
        market_cap: typing.Callable[[], T_Result],
        v3depth: typing.Callable[[], T_Result],
        v4depth: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdMarketsRequestSort.VOLUME:
            return volume()
        if self is GetChainsChainIdMarketsRequestSort.SWAPS:
            return swaps()
        if self is GetChainsChainIdMarketsRequestSort.MARKET_CAP:
            return market_cap()
        if self is GetChainsChainIdMarketsRequestSort.V3DEPTH:
            return v3depth()
        if self is GetChainsChainIdMarketsRequestSort.V4DEPTH:
            return v4depth()
        if self is GetChainsChainIdMarketsRequestSort.NAME:
            return name()
