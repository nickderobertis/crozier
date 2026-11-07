

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelHealth(enum.StrEnum):
    UNKNOWN = "unknown"
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNAVAILABLE = "unavailable"

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        healthy: typing.Callable[[], T_Result],
        degraded: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChannelHealth.UNKNOWN:
            return unknown()
        if self is ChannelHealth.HEALTHY:
            return healthy()
        if self is ChannelHealth.DEGRADED:
            return degraded()
        if self is ChannelHealth.UNAVAILABLE:
            return unavailable()
