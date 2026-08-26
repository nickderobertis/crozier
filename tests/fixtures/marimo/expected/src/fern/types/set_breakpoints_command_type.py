

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SetBreakpointsCommandType(enum.StrEnum):
    SET_BREAKPOINTS = "set-breakpoints"

    def visit(self, set_breakpoints: typing.Callable[[], T_Result]) -> T_Result:
        if self is SetBreakpointsCommandType.SET_BREAKPOINTS:
            return set_breakpoints()
