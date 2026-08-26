

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServerConfigTransport(enum.StrEnum):
    SSE = "sse"
    WEBSOCKET = "websocket"

    def visit(self, sse: typing.Callable[[], T_Result], websocket: typing.Callable[[], T_Result]) -> T_Result:
        if self is ServerConfigTransport.SSE:
            return sse()
        if self is ServerConfigTransport.WEBSOCKET:
            return websocket()
