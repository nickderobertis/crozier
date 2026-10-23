

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdStatusResponseSwapIndexerCoverageScope(enum.StrEnum):
    PRIORITY_POOLS = "priority_pools"

    def visit(self, priority_pools: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetChainsChainIdStatusResponseSwapIndexerCoverageScope.PRIORITY_POOLS:
            return priority_pools()
