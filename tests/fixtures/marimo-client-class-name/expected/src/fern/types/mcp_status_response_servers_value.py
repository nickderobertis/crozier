

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class McpStatusResponseServersValue(enum.StrEnum):
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"
    FAILED = "failed"
    PENDING = "pending"

    def visit(
        self,
        connected: typing.Callable[[], T_Result],
        disconnected: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is McpStatusResponseServersValue.CONNECTED:
            return connected()
        if self is McpStatusResponseServersValue.DISCONNECTED:
            return disconnected()
        if self is McpStatusResponseServersValue.FAILED:
            return failed()
        if self is McpStatusResponseServersValue.PENDING:
            return pending()
