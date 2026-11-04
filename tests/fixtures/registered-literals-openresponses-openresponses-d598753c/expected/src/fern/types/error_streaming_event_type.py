

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ErrorStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `error`.
    """

    ERROR = "error"

    def visit(self, error: typing.Callable[[], T_Result]) -> T_Result:
        if self is ErrorStreamingEventType.ERROR:
            return error()
