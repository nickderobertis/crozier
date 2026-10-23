

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetStatusResponseVerdict(enum.StrEnum):
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
        if self is GetStatusResponseVerdict.LIVE:
            return live()
        if self is GetStatusResponseVerdict.DEGRADED:
            return degraded()
        if self is GetStatusResponseVerdict.STALE:
            return stale()
        if self is GetStatusResponseVerdict.NEVER:
            return never()
