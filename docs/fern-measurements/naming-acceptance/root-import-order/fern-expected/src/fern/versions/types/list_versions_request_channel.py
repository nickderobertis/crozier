

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListVersionsRequestChannel(enum.StrEnum):
    STABLE = "stable"
    BETA = "beta"

    def visit(self, stable: typing.Callable[[], T_Result], beta: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListVersionsRequestChannel.STABLE:
            return stable()
        if self is ListVersionsRequestChannel.BETA:
            return beta()
