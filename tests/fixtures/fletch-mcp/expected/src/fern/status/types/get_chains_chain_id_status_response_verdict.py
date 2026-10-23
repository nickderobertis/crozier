

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdStatusResponseVerdict(enum.StrEnum):
    LIVE = "live"
    DEGRADED = "degraded"
    STALE = "stale"
    NEVER = "never"

    def visit(
        self,
        live: typing.Callable[[], T_Result],
        degraded: typing.Callable[[], T_Result],
        stale: typing.Callable[[], T_Result],
        never: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdStatusResponseVerdict.LIVE:
            return live()
        if self is GetChainsChainIdStatusResponseVerdict.DEGRADED:
            return degraded()
        if self is GetChainsChainIdStatusResponseVerdict.STALE:
            return stale()
        if self is GetChainsChainIdStatusResponseVerdict.NEVER:
            return never()
