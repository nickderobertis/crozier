

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdStatusResponseSwapIndexerTiersScope(enum.StrEnum):
    CANONICAL_CATALOG_POOLS = "canonical_catalog_pools"

    def visit(self, canonical_catalog_pools: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetChainsChainIdStatusResponseSwapIndexerTiersScope.CANONICAL_CATALOG_POOLS:
            return canonical_catalog_pools()
