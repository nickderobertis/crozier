

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdDexPoolsRequestTier(enum.StrEnum):
    ACTIVE = "active"
    QUIET = "quiet"
    DORMANT = "dormant"
    ALL = "all"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        quiet: typing.Callable[[], T_Result],
        dormant: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdDexPoolsRequestTier.ACTIVE:
            return active()
        if self is GetChainsChainIdDexPoolsRequestTier.QUIET:
            return quiet()
        if self is GetChainsChainIdDexPoolsRequestTier.DORMANT:
            return dormant()
        if self is GetChainsChainIdDexPoolsRequestTier.ALL:
            return all_()
