

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RateLimitErrorErrorCode(enum.StrEnum):
    RATE_LIMIT_EXCEEDED = "RATE_LIMIT_EXCEEDED"

    def visit(self, rate_limit_exceeded: typing.Callable[[], T_Result]) -> T_Result:
        if self is RateLimitErrorErrorCode.RATE_LIMIT_EXCEEDED:
            return rate_limit_exceeded()
