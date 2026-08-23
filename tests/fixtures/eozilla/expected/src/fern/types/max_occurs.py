

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MaxOccurs(enum.StrEnum):
    UNBOUNDED = "unbounded"

    def visit(self, unbounded: typing.Callable[[], T_Result]) -> T_Result:
        if self is MaxOccurs.UNBOUNDED:
            return unbounded()
