

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListAggregatedWptMetricsRequestChannel(enum.StrEnum):
    STABLE = "stable"
    EXPERIMENTAL = "experimental"

    def visit(self, stable: typing.Callable[[], T_Result], experimental: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListAggregatedWptMetricsRequestChannel.STABLE:
            return stable()
        if self is ListAggregatedWptMetricsRequestChannel.EXPERIMENTAL:
            return experimental()
