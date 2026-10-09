

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class McpServerInitInfoTransportType(enum.StrEnum):
    """
    Transport used to connect to the MCP server.
    """

    STREAMABLE_HTTP = "streamable-http"
    SSE = "sse"

    def visit(self, streamable_http: typing.Callable[[], T_Result], sse: typing.Callable[[], T_Result]) -> T_Result:
        if self is McpServerInitInfoTransportType.STREAMABLE_HTTP:
            return streamable_http()
        if self is McpServerInitInfoTransportType.SSE:
            return sse()
