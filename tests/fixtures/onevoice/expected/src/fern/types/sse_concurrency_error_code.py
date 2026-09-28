

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SseConcurrencyErrorCode(enum.StrEnum):
    SSE_CONCURRENCY_EXCEEDED = "sse_concurrency_exceeded"

    def visit(self, sse_concurrency_exceeded: typing.Callable[[], T_Result]) -> T_Result:
        if self is SseConcurrencyErrorCode.SSE_CONCURRENCY_EXCEEDED:
            return sse_concurrency_exceeded()
