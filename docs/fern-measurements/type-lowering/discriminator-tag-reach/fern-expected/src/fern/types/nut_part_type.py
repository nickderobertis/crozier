

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NutPartType(enum.StrEnum):
    NUT = "NUT"

    def visit(self, nut: typing.Callable[[], T_Result]) -> T_Result:
        if self is NutPartType.NUT:
            return nut()
