

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResourcesSearchGetError400ErrorCode(enum.StrEnum):
    BAD_REQUEST = "BAD_REQUEST"
    MISSING_PARAMETER = "MISSING_PARAMETER"
    INVALID_PARAMETER = "INVALID_PARAMETER"
    VALIDATION_ERROR = "VALIDATION_ERROR"

    def visit(
        self,
        bad_request: typing.Callable[[], T_Result],
        missing_parameter: typing.Callable[[], T_Result],
        invalid_parameter: typing.Callable[[], T_Result],
        validation_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResourcesSearchGetError400ErrorCode.BAD_REQUEST:
            return bad_request()
        if self is ResourcesSearchGetError400ErrorCode.MISSING_PARAMETER:
            return missing_parameter()
        if self is ResourcesSearchGetError400ErrorCode.INVALID_PARAMETER:
            return invalid_parameter()
        if self is ResourcesSearchGetError400ErrorCode.VALIDATION_ERROR:
            return validation_error()
