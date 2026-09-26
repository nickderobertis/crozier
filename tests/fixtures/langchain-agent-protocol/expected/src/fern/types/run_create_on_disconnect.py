

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunCreateOnDisconnect(enum.StrEnum):
    """
    The disconnect mode to use. Must be one of 'cancel' or 'continue'.
    """

    CANCEL = "cancel"
    CONTINUE = "continue"

    def visit(self, cancel: typing.Callable[[], T_Result], continue_: typing.Callable[[], T_Result]) -> T_Result:
        if self is RunCreateOnDisconnect.CANCEL:
            return cancel()
        if self is RunCreateOnDisconnect.CONTINUE:
            return continue_()
