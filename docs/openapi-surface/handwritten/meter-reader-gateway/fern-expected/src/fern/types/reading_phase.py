

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReadingPhase(enum.StrEnum):
    SINGLE = "single"
    THREE = "three"

    def visit(self, single: typing.Callable[[], T_Result], three: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReadingPhase.SINGLE:
            return single()
        if self is ReadingPhase.THREE:
            return three()
