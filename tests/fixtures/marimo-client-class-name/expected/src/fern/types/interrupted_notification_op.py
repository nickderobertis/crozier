

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InterruptedNotificationOp(enum.StrEnum):
    INTERRUPTED = "interrupted"

    def visit(self, interrupted: typing.Callable[[], T_Result]) -> T_Result:
        if self is InterruptedNotificationOp.INTERRUPTED:
            return interrupted()
