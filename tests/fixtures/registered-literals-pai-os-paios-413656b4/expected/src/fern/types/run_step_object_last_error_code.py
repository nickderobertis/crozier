

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunStepObjectLastErrorCode(enum.StrEnum):
    """
    One of `server_error` or `rate_limit_exceeded`.
    """

    SERVER_ERROR = "server_error"
    RATE_LIMIT_EXCEEDED = "rate_limit_exceeded"

    def visit(
        self, server_error: typing.Callable[[], T_Result], rate_limit_exceeded: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is RunStepObjectLastErrorCode.SERVER_ERROR:
            return server_error()
        if self is RunStepObjectLastErrorCode.RATE_LIMIT_EXCEEDED:
            return rate_limit_exceeded()
