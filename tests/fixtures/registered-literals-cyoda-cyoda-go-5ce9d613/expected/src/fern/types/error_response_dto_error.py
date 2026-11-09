

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ErrorResponseDtoError(enum.StrEnum):
    """
    Error codes from RFC 6749 Section 5.2 (OAuth 2.0 Error Response) identifying the type of error
    """

    INVALID_REQUEST = "invalid_request"
    INVALID_CLIENT = "invalid_client"
    INVALID_GRANT = "invalid_grant"
    UNAUTHORIZED_CLIENT = "unauthorized_client"
    UNSUPPORTED_GRANT_TYPE = "unsupported_grant_type"
    INVALID_SCOPE = "invalid_scope"
    ACCESS_DENIED = "access_denied"

    def visit(
        self,
        invalid_request: typing.Callable[[], T_Result],
        invalid_client: typing.Callable[[], T_Result],
        invalid_grant: typing.Callable[[], T_Result],
        unauthorized_client: typing.Callable[[], T_Result],
        unsupported_grant_type: typing.Callable[[], T_Result],
        invalid_scope: typing.Callable[[], T_Result],
        access_denied: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ErrorResponseDtoError.INVALID_REQUEST:
            return invalid_request()
        if self is ErrorResponseDtoError.INVALID_CLIENT:
            return invalid_client()
        if self is ErrorResponseDtoError.INVALID_GRANT:
            return invalid_grant()
        if self is ErrorResponseDtoError.UNAUTHORIZED_CLIENT:
            return unauthorized_client()
        if self is ErrorResponseDtoError.UNSUPPORTED_GRANT_TYPE:
            return unsupported_grant_type()
        if self is ErrorResponseDtoError.INVALID_SCOPE:
            return invalid_scope()
        if self is ErrorResponseDtoError.ACCESS_DENIED:
            return access_denied()
