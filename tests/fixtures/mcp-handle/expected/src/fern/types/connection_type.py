

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConnectionType(enum.StrEnum):
    SSE = "SSE"
    STREAMABLE_HTTP = "StreamableHttp"

    def visit(self, sse: typing.Callable[[], T_Result], streamable_http: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConnectionType.SSE:
            return sse()
        if self is ConnectionType.STREAMABLE_HTTP:
            return streamable_http()
