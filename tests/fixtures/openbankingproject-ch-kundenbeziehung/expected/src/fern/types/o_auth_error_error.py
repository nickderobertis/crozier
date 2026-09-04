

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OAuthErrorError(enum.StrEnum):
    INVALID_REQUEST = "invalid_request"
    INVALID_CLIENT = "invalid_client"
    INVALID_GRANT = "invalid_grant"
    UNAUTHORIZED_CLIENT = "unauthorized_client"
    UNSUPPORTED_GRANT_TYPE = "unsupported_grant_type"
    INVALID_SCOPE = "invalid_scope"
    SERVER_ERROR = "server_error"
    TEMPORARILY_UNAVAILABLE = "temporarily_unavailable"

    def visit(
        self,
        invalid_request: typing.Callable[[], T_Result],
        invalid_client: typing.Callable[[], T_Result],
        invalid_grant: typing.Callable[[], T_Result],
        unauthorized_client: typing.Callable[[], T_Result],
        unsupported_grant_type: typing.Callable[[], T_Result],
        invalid_scope: typing.Callable[[], T_Result],
        server_error: typing.Callable[[], T_Result],
        temporarily_unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OAuthErrorError.INVALID_REQUEST:
            return invalid_request()
        if self is OAuthErrorError.INVALID_CLIENT:
            return invalid_client()
        if self is OAuthErrorError.INVALID_GRANT:
            return invalid_grant()
        if self is OAuthErrorError.UNAUTHORIZED_CLIENT:
            return unauthorized_client()
        if self is OAuthErrorError.UNSUPPORTED_GRANT_TYPE:
            return unsupported_grant_type()
        if self is OAuthErrorError.INVALID_SCOPE:
            return invalid_scope()
        if self is OAuthErrorError.SERVER_ERROR:
            return server_error()
        if self is OAuthErrorError.TEMPORARILY_UNAVAILABLE:
            return temporarily_unavailable()
