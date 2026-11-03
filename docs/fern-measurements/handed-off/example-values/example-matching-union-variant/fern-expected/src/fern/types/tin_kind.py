

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TinKind(enum.StrEnum):
    TIN = "tin"

    def visit(self, tin: typing.Callable[[], T_Result]) -> T_Result:
        if self is TinKind.TIN:
            return tin()
