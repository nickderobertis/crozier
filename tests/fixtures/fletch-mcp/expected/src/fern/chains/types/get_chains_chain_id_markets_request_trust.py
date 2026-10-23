

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdMarketsRequestTrust(enum.StrEnum):
    ALL = "all"
    VERIFIED = "verified"
    LISTED = "listed"
    COMMUNITY = "community"
    LOOKALIKE = "lookalike"
    UNKNOWN = "unknown"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        verified: typing.Callable[[], T_Result],
        listed: typing.Callable[[], T_Result],
        community: typing.Callable[[], T_Result],
        lookalike: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdMarketsRequestTrust.ALL:
            return all_()
        if self is GetChainsChainIdMarketsRequestTrust.VERIFIED:
            return verified()
        if self is GetChainsChainIdMarketsRequestTrust.LISTED:
            return listed()
        if self is GetChainsChainIdMarketsRequestTrust.COMMUNITY:
            return community()
        if self is GetChainsChainIdMarketsRequestTrust.LOOKALIKE:
            return lookalike()
        if self is GetChainsChainIdMarketsRequestTrust.UNKNOWN:
            return unknown()
