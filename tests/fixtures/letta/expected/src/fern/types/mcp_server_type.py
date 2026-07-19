

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class McpServerType(enum.StrEnum):
    SSE = "sse"
    STDIO = "stdio"
    STREAMABLE_HTTP = "streamable_http"

    def visit(
        self,
        sse: typing.Callable[[], T_Result],
        stdio: typing.Callable[[], T_Result],
        streamable_http: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is McpServerType.SSE:
            return sse()
        if self is McpServerType.STDIO:
            return stdio()
        if self is McpServerType.STREAMABLE_HTTP:
            return streamable_http()
