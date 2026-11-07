

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebSocketErrorEventType(enum.StrEnum):
    """
    The event type. Always `error`.
    """

    ERROR = "error"

    def visit(self, error: typing.Callable[[], T_Result]) -> T_Result:
        if self is WebSocketErrorEventType.ERROR:
            return error()
