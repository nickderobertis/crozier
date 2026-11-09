

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunObjectLastErrorCode(enum.StrEnum):
    """
    One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.
    """

    SERVER_ERROR = "server_error"
    RATE_LIMIT_EXCEEDED = "rate_limit_exceeded"
    INVALID_PROMPT = "invalid_prompt"

    def visit(
        self,
        server_error: typing.Callable[[], T_Result],
        rate_limit_exceeded: typing.Callable[[], T_Result],
        invalid_prompt: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunObjectLastErrorCode.SERVER_ERROR:
            return server_error()
        if self is RunObjectLastErrorCode.RATE_LIMIT_EXCEEDED:
            return rate_limit_exceeded()
        if self is RunObjectLastErrorCode.INVALID_PROMPT:
            return invalid_prompt()
