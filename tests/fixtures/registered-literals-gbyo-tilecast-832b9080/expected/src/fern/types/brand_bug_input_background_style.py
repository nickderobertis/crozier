

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BrandBugInputBackgroundStyle(enum.StrEnum):
    NONE = "none"
    SCRIM = "scrim"

    def visit(self, none: typing.Callable[[], T_Result], scrim: typing.Callable[[], T_Result]) -> T_Result:
        if self is BrandBugInputBackgroundStyle.NONE:
            return none()
        if self is BrandBugInputBackgroundStyle.SCRIM:
            return scrim()
