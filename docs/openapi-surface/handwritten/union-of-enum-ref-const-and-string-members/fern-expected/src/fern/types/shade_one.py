

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ShadeOne(enum.StrEnum):
    INDIGO = "indigo"

    def visit(self, indigo: typing.Callable[[], T_Result]) -> T_Result:
        if self is ShadeOne.INDIGO:
            return indigo()
