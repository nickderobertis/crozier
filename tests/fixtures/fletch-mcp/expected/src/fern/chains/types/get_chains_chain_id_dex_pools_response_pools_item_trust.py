

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdDexPoolsResponsePoolsItemTrust(enum.StrEnum):
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
        if self is GetChainsChainIdDexPoolsResponsePoolsItemTrust.VERIFIED:
            return verified()
        if self is GetChainsChainIdDexPoolsResponsePoolsItemTrust.LISTED:
            return listed()
        if self is GetChainsChainIdDexPoolsResponsePoolsItemTrust.COMMUNITY:
            return community()
        if self is GetChainsChainIdDexPoolsResponsePoolsItemTrust.LOOKALIKE:
            return lookalike()
        if self is GetChainsChainIdDexPoolsResponsePoolsItemTrust.UNKNOWN:
            return unknown()
