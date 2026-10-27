

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SingleBranchTest(enum.StrEnum):
    X = "x"
    Y = "y"

    def visit(self, x: typing.Callable[[], T_Result], y: typing.Callable[[], T_Result]) -> T_Result:
        if self is SingleBranchTest.X:
            return x()
        if self is SingleBranchTest.Y:
            return y()
