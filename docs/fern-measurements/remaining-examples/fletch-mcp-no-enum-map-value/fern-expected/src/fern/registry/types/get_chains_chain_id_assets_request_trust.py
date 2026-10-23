

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdAssetsRequestTrust(enum.StrEnum):
    VERIFIED = "verified"
    LISTED = "listed"
    LOOKALIKE = "lookalike"
    COMMUNITY = "community"
    UNKNOWN = "unknown"

    def visit(
        self,
        verified: typing.Callable[[], T_Result],
        listed: typing.Callable[[], T_Result],
        lookalike: typing.Callable[[], T_Result],
        community: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdAssetsRequestTrust.VERIFIED:
            return verified()
        if self is GetChainsChainIdAssetsRequestTrust.LISTED:
            return listed()
        if self is GetChainsChainIdAssetsRequestTrust.LOOKALIKE:
            return lookalike()
        if self is GetChainsChainIdAssetsRequestTrust.COMMUNITY:
            return community()
        if self is GetChainsChainIdAssetsRequestTrust.UNKNOWN:
            return unknown()
