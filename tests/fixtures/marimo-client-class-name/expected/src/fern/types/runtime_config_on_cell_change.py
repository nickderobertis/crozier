

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RuntimeConfigOnCellChange(enum.StrEnum):
    AUTORUN = "autorun"
    LAZY = "lazy"

    def visit(self, autorun: typing.Callable[[], T_Result], lazy: typing.Callable[[], T_Result]) -> T_Result:
        if self is RuntimeConfigOnCellChange.AUTORUN:
            return autorun()
        if self is RuntimeConfigOnCellChange.LAZY:
            return lazy()
