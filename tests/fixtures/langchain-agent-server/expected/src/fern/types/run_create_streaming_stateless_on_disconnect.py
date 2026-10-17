

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunCreateStreamingStatelessOnDisconnect(enum.StrEnum):
    """
    The disconnect mode to use. Must be one of 'cancel' or 'continue'.
    """

    CANCEL = "cancel"
    CONTINUE = "continue"

    def visit(self, cancel: typing.Callable[[], T_Result], continue_: typing.Callable[[], T_Result]) -> T_Result:
        if self is RunCreateStreamingStatelessOnDisconnect.CANCEL:
            return cancel()
        if self is RunCreateStreamingStatelessOnDisconnect.CONTINUE:
            return continue_()
