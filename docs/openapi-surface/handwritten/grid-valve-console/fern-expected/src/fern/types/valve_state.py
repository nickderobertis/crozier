

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ValveState(enum.StrEnum):
    OPEN = "open"
    SHUT = "shut"
    STUCK = "stuck"

    def visit(
        self,
        open: typing.Callable[[], T_Result],
        shut: typing.Callable[[], T_Result],
        stuck: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ValveState.OPEN:
            return open()
        if self is ValveState.SHUT:
            return shut()
        if self is ValveState.STUCK:
            return stuck()
