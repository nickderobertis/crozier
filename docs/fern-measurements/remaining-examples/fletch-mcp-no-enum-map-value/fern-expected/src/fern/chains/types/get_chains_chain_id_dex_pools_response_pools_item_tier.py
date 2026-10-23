

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdDexPoolsResponsePoolsItemTier(enum.StrEnum):
    """
    Active pools are prioritized for background sampling; quiet pools receive a daily cycle; dormant pools receive demand-driven reads. Scheduling does not establish freshness: inspect stateCheckedAt and stateCurrent.
    """

    ACTIVE = "active"
    QUIET = "quiet"
    DORMANT = "dormant"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        quiet: typing.Callable[[], T_Result],
        dormant: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdDexPoolsResponsePoolsItemTier.ACTIVE:
            return active()
        if self is GetChainsChainIdDexPoolsResponsePoolsItemTier.QUIET:
            return quiet()
        if self is GetChainsChainIdDexPoolsResponsePoolsItemTier.DORMANT:
            return dormant()
