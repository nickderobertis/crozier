

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActiveLineNotificationOp(enum.StrEnum):
    ACTIVE_LINE = "active-line"

    def visit(self, active_line: typing.Callable[[], T_Result]) -> T_Result:
        if self is ActiveLineNotificationOp.ACTIVE_LINE:
            return active_line()
