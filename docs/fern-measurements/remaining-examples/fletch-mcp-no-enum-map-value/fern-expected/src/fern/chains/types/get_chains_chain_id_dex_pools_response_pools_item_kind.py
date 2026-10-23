

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdDexPoolsResponsePoolsItemKind(enum.StrEnum):
    """
    Alias of trust for the priced token. Listing membership is separate.
    """

    VERIFIED = "verified"
    LISTED = "listed"
    COMMUNITY = "community"
    LOOKALIKE = "lookalike"
    UNKNOWN = "unknown"

    def visit(
        self,
        verified: typing.Callable[[], T_Result],
        listed: typing.Callable[[], T_Result],
        community: typing.Callable[[], T_Result],
        lookalike: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdDexPoolsResponsePoolsItemKind.VERIFIED:
            return verified()
        if self is GetChainsChainIdDexPoolsResponsePoolsItemKind.LISTED:
            return listed()
        if self is GetChainsChainIdDexPoolsResponsePoolsItemKind.COMMUNITY:
            return community()
        if self is GetChainsChainIdDexPoolsResponsePoolsItemKind.LOOKALIKE:
            return lookalike()
        if self is GetChainsChainIdDexPoolsResponsePoolsItemKind.UNKNOWN:
            return unknown()
