

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CastingStartMode(enum.StrEnum):
    ORIGINAL = "original"
    VIDEO = "video"

    def visit(self, original: typing.Callable[[], T_Result], video: typing.Callable[[], T_Result]) -> T_Result:
        if self is CastingStartMode.ORIGINAL:
            return original()
        if self is CastingStartMode.VIDEO:
            return video()
