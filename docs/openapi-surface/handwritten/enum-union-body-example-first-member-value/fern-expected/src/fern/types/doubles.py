

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Doubles(enum.StrEnum):
    GRANDSIRE = "grandsire"
    STEDMAN = "stedman"

    def visit(self, grandsire: typing.Callable[[], T_Result], stedman: typing.Callable[[], T_Result]) -> T_Result:
        if self is Doubles.GRANDSIRE:
            return grandsire()
        if self is Doubles.STEDMAN:
            return stedman()
