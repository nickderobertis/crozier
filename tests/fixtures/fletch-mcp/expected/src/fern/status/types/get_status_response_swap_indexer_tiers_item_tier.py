

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetStatusResponseSwapIndexerTiersItemTier(enum.StrEnum):
    ACTIVE = "active"
    QUIET = "quiet"
    DORMANT = "dormant"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        quiet: typing.Callable[[], T_Result],
        dormant: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetStatusResponseSwapIndexerTiersItemTier.ACTIVE:
            return active()
        if self is GetStatusResponseSwapIndexerTiersItemTier.QUIET:
            return quiet()
        if self is GetStatusResponseSwapIndexerTiersItemTier.DORMANT:
            return dormant()
