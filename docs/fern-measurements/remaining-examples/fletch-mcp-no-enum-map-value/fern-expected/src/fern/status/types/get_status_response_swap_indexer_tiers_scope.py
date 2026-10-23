

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetStatusResponseSwapIndexerTiersScope(enum.StrEnum):
    CANONICAL_CATALOG_POOLS = "canonical_catalog_pools"

    def visit(self, canonical_catalog_pools: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetStatusResponseSwapIndexerTiersScope.CANONICAL_CATALOG_POOLS:
            return canonical_catalog_pools()
