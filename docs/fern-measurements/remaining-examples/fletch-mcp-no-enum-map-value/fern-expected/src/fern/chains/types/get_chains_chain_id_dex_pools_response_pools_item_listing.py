

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdDexPoolsResponsePoolsItemListing(enum.StrEnum):
    LISTED = "listed"
    UNLISTED = "unlisted"

    def visit(self, listed: typing.Callable[[], T_Result], unlisted: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetChainsChainIdDexPoolsResponsePoolsItemListing.LISTED:
            return listed()
        if self is GetChainsChainIdDexPoolsResponsePoolsItemListing.UNLISTED:
            return unlisted()
