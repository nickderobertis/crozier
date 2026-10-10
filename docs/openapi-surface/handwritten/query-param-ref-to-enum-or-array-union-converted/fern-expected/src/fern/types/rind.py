

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Rind(enum.StrEnum):
    WASHED = "washed"
    BLOOMY = "bloomy"

    def visit(self, washed: typing.Callable[[], T_Result], bloomy: typing.Callable[[], T_Result]) -> T_Result:
        if self is Rind.WASHED:
            return washed()
        if self is Rind.BLOOMY:
            return bloomy()
