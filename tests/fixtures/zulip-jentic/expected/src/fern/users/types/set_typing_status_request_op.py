

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SetTypingStatusRequestOp(enum.StrEnum):
    """
    Whether the user has started (`"start"`) or stopped (`"stop"`) typing.
    """

    START = "start"
    STOP = "stop"

    def visit(self, start: typing.Callable[[], T_Result], stop: typing.Callable[[], T_Result]) -> T_Result:
        if self is SetTypingStatusRequestOp.START:
            return start()
        if self is SetTypingStatusRequestOp.STOP:
            return stop()
