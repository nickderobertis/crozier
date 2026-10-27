

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReadingPlacementBand(enum.StrEnum):
    NEAR = "near"
    FAR = "far"

    def visit(self, near: typing.Callable[[], T_Result], far: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReadingPlacementBand.NEAR:
            return near()
        if self is ReadingPlacementBand.FAR:
            return far()
