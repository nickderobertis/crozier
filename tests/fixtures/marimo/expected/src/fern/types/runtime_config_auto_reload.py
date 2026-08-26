

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RuntimeConfigAutoReload(enum.StrEnum):
    AUTORUN = "autorun"
    LAZY = "lazy"
    OFF = "off"

    def visit(
        self,
        autorun: typing.Callable[[], T_Result],
        lazy: typing.Callable[[], T_Result],
        off: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RuntimeConfigAutoReload.AUTORUN:
            return autorun()
        if self is RuntimeConfigAutoReload.LAZY:
            return lazy()
        if self is RuntimeConfigAutoReload.OFF:
            return off()
