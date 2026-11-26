

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TerrierSize(enum.StrEnum):
    TOY = "toy"
    STANDARD = "standard"

    def visit(self, toy: typing.Callable[[], T_Result], standard: typing.Callable[[], T_Result]) -> T_Result:
        if self is TerrierSize.TOY:
            return toy()
        if self is TerrierSize.STANDARD:
            return standard()
