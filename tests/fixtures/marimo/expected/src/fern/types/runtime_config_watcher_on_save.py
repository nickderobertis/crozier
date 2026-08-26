

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RuntimeConfigWatcherOnSave(enum.StrEnum):
    AUTORUN = "autorun"
    LAZY = "lazy"

    def visit(self, autorun: typing.Callable[[], T_Result], lazy: typing.Callable[[], T_Result]) -> T_Result:
        if self is RuntimeConfigWatcherOnSave.AUTORUN:
            return autorun()
        if self is RuntimeConfigWatcherOnSave.LAZY:
            return lazy()
