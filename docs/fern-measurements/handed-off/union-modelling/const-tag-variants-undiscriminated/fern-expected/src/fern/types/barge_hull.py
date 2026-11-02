

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BargeHull(enum.StrEnum):
    BARGE = "barge"

    def visit(self, barge: typing.Callable[[], T_Result]) -> T_Result:
        if self is BargeHull.BARGE:
            return barge()
