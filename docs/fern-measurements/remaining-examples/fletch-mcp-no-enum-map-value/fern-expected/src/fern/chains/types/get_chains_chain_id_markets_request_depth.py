

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdMarketsRequestDepth(enum.StrEnum):
    ALL = "all"
    V310K = "v3_10k"
    V3100K = "v3_100k"
    V41K = "v4_1k"
    V410K = "v4_10k"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        v310k: typing.Callable[[], T_Result],
        v3100k: typing.Callable[[], T_Result],
        v41k: typing.Callable[[], T_Result],
        v410k: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdMarketsRequestDepth.ALL:
            return all_()
        if self is GetChainsChainIdMarketsRequestDepth.V310K:
            return v310k()
        if self is GetChainsChainIdMarketsRequestDepth.V3100K:
            return v3100k()
        if self is GetChainsChainIdMarketsRequestDepth.V41K:
            return v41k()
        if self is GetChainsChainIdMarketsRequestDepth.V410K:
            return v410k()
