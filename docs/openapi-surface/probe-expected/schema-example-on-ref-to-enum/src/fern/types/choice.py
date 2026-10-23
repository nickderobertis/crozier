

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Choice(enum.StrEnum):
    ALPHA = "alpha"
    BETA = "beta"

    def visit(self, alpha: typing.Callable[[], T_Result], beta: typing.Callable[[], T_Result]) -> T_Result:
        if self is Choice.ALPHA:
            return alpha()
        if self is Choice.BETA:
            return beta()
