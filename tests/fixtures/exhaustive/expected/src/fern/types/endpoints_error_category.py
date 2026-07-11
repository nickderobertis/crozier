

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EndpointsErrorCategory(str, enum.Enum):
    API_ERROR = "API_ERROR"
    AUTHENTICATION_ERROR = "AUTHENTICATION_ERROR"
    INVALID_REQUEST_ERROR = "INVALID_REQUEST_ERROR"

    def visit(
        self,
        api_error: typing.Callable[[], T_Result],
        authentication_error: typing.Callable[[], T_Result],
        invalid_request_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EndpointsErrorCategory.API_ERROR:
            return api_error()
        if self is EndpointsErrorCategory.AUTHENTICATION_ERROR:
            return authentication_error()
        if self is EndpointsErrorCategory.INVALID_REQUEST_ERROR:
            return invalid_request_error()
