

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OAuth2ErrorError(enum.StrEnum):
    """
    RFC 8693 error code.
    """

    INVALID_REQUEST = "invalid_request"
    INVALID_CLIENT = "invalid_client"
    INVALID_GRANT = "invalid_grant"
    INVALID_TARGET = "invalid_target"
    ACCESS_DENIED = "access_denied"
    SERVER_ERROR = "server_error"

    def visit(
        self,
        invalid_request: typing.Callable[[], T_Result],
        invalid_client: typing.Callable[[], T_Result],
        invalid_grant: typing.Callable[[], T_Result],
        invalid_target: typing.Callable[[], T_Result],
        access_denied: typing.Callable[[], T_Result],
        server_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OAuth2ErrorError.INVALID_REQUEST:
            return invalid_request()
        if self is OAuth2ErrorError.INVALID_CLIENT:
            return invalid_client()
        if self is OAuth2ErrorError.INVALID_GRANT:
            return invalid_grant()
        if self is OAuth2ErrorError.INVALID_TARGET:
            return invalid_target()
        if self is OAuth2ErrorError.ACCESS_DENIED:
            return access_denied()
        if self is OAuth2ErrorError.SERVER_ERROR:
            return server_error()
