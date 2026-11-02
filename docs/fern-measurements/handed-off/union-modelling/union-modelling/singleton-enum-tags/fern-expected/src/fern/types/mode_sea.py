

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModeSea(enum.StrEnum):
    SEA = "sea"

    def visit(self, sea: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModeSea.SEA:
            return sea()
