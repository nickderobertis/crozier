

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScalarDefaultsMode(enum.StrEnum):
    ALPHA = "alpha"
    BETA = "beta"

    def visit(self, alpha: typing.Callable[[], T_Result], beta: typing.Callable[[], T_Result]) -> T_Result:
        if self is ScalarDefaultsMode.ALPHA:
            return alpha()
        if self is ScalarDefaultsMode.BETA:
            return beta()
