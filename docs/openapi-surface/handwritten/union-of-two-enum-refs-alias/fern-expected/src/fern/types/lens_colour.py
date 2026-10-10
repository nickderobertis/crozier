

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LensColour(enum.StrEnum):
    AMBER = "amber"
    WHITE = "white"

    def visit(self, amber: typing.Callable[[], T_Result], white: typing.Callable[[], T_Result]) -> T_Result:
        if self is LensColour.AMBER:
            return amber()
        if self is LensColour.WHITE:
            return white()
