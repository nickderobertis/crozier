

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Uvw(enum.StrEnum):
    LIT = "lit"
    UNLIT = "unlit"

    def visit(self, lit: typing.Callable[[], T_Result], unlit: typing.Callable[[], T_Result]) -> T_Result:
        if self is Uvw.LIT:
            return lit()
        if self is Uvw.UNLIT:
            return unlit()
