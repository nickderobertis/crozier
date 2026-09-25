

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TableFormerMode(enum.StrEnum):
    FAST = "fast"
    ACCURATE = "accurate"

    def visit(self, fast: typing.Callable[[], T_Result], accurate: typing.Callable[[], T_Result]) -> T_Result:
        if self is TableFormerMode.FAST:
            return fast()
        if self is TableFormerMode.ACCURATE:
            return accurate()
