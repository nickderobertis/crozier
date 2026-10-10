

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VideoSourceType(enum.StrEnum):
    PROGRESSIVE = "progressive"
    ADAPTIVE = "adaptive"
    FRAGMENTED = "fragmented"
    UNKNOWN = "unknown"

    def visit(
        self,
        progressive: typing.Callable[[], T_Result],
        adaptive: typing.Callable[[], T_Result],
        fragmented: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VideoSourceType.PROGRESSIVE:
            return progressive()
        if self is VideoSourceType.ADAPTIVE:
            return adaptive()
        if self is VideoSourceType.FRAGMENTED:
            return fragmented()
        if self is VideoSourceType.UNKNOWN:
            return unknown()
