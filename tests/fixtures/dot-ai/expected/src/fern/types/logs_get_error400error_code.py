

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LogsGetError400ErrorCode(enum.StrEnum):
    BAD_REQUEST = "BAD_REQUEST"
    INVALID_PARAMETER = "INVALID_PARAMETER"

    def visit(
        self, bad_request: typing.Callable[[], T_Result], invalid_parameter: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is LogsGetError400ErrorCode.BAD_REQUEST:
            return bad_request()
        if self is LogsGetError400ErrorCode.INVALID_PARAMETER:
            return invalid_parameter()
