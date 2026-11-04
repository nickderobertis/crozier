

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebSocketResponseCreateEventType(enum.StrEnum):
    """
    The client event type. Always `response.create`.
    """

    RESPONSE_CREATE = "response.create"

    def visit(self, response_create: typing.Callable[[], T_Result]) -> T_Result:
        if self is WebSocketResponseCreateEventType.RESPONSE_CREATE:
            return response_create()
