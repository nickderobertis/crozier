

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunCreateStreamingStatefulOnDisconnect(enum.StrEnum):
    """
    The disconnect mode to use. Must be one of 'cancel' or 'continue'.
    """

    CANCEL = "cancel"
    CONTINUE = "continue"

    def visit(self, cancel: typing.Callable[[], T_Result], continue_: typing.Callable[[], T_Result]) -> T_Result:
        if self is RunCreateStreamingStatefulOnDisconnect.CANCEL:
            return cancel()
        if self is RunCreateStreamingStatefulOnDisconnect.CONTINUE:
            return continue_()
