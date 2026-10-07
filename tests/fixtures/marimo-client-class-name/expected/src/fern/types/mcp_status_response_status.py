

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class McpStatusResponseStatus(enum.StrEnum):
    ERROR = "error"
    OK = "ok"
    PARTIAL = "partial"

    def visit(
        self,
        error: typing.Callable[[], T_Result],
        ok: typing.Callable[[], T_Result],
        partial: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is McpStatusResponseStatus.ERROR:
            return error()
        if self is McpStatusResponseStatus.OK:
            return ok()
        if self is McpStatusResponseStatus.PARTIAL:
            return partial()
