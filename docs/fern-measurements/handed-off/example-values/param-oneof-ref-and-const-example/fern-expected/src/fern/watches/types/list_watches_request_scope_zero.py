

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListWatchesRequestScopeZero(enum.StrEnum):
    MINE = "mine"

    def visit(self, mine: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListWatchesRequestScopeZero.MINE:
            return mine()
