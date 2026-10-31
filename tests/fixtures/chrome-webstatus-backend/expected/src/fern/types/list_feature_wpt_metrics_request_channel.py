

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListFeatureWptMetricsRequestChannel(enum.StrEnum):
    STABLE = "stable"
    EXPERIMENTAL = "experimental"

    def visit(self, stable: typing.Callable[[], T_Result], experimental: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListFeatureWptMetricsRequestChannel.STABLE:
            return stable()
        if self is ListFeatureWptMetricsRequestChannel.EXPERIMENTAL:
            return experimental()
