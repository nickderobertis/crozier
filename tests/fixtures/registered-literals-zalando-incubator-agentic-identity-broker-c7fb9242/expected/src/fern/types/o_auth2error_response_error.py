

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OAuth2ErrorResponseError(enum.StrEnum):
    """
    OAuth2 error code as per RFC 6749.
    Machine-readable code for programmatic error handling.
    """

    INVALID_REQUEST = "invalid_request"
    INVALID_REDIRECT_URI = "invalid_redirect_uri"
    UNAUTHORIZED_CLIENT = "unauthorized_client"
    ACCESS_DENIED = "access_denied"
    UNSUPPORTED_RESPONSE_TYPE = "unsupported_response_type"
    INVALID_SCOPE = "invalid_scope"
    SERVER_ERROR = "server_error"
    TEMPORARILY_UNAVAILABLE = "temporarily_unavailable"
    INVALID_CLIENT = "invalid_client"
    INVALID_GRANT = "invalid_grant"
    UNSUPPORTED_GRANT_TYPE = "unsupported_grant_type"

    def visit(
        self,
        invalid_request: typing.Callable[[], T_Result],
        invalid_redirect_uri: typing.Callable[[], T_Result],
        unauthorized_client: typing.Callable[[], T_Result],
        access_denied: typing.Callable[[], T_Result],
        unsupported_response_type: typing.Callable[[], T_Result],
        invalid_scope: typing.Callable[[], T_Result],
        server_error: typing.Callable[[], T_Result],
        temporarily_unavailable: typing.Callable[[], T_Result],
        invalid_client: typing.Callable[[], T_Result],
        invalid_grant: typing.Callable[[], T_Result],
        unsupported_grant_type: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OAuth2ErrorResponseError.INVALID_REQUEST:
            return invalid_request()
        if self is OAuth2ErrorResponseError.INVALID_REDIRECT_URI:
            return invalid_redirect_uri()
        if self is OAuth2ErrorResponseError.UNAUTHORIZED_CLIENT:
            return unauthorized_client()
        if self is OAuth2ErrorResponseError.ACCESS_DENIED:
            return access_denied()
        if self is OAuth2ErrorResponseError.UNSUPPORTED_RESPONSE_TYPE:
            return unsupported_response_type()
        if self is OAuth2ErrorResponseError.INVALID_SCOPE:
            return invalid_scope()
        if self is OAuth2ErrorResponseError.SERVER_ERROR:
            return server_error()
        if self is OAuth2ErrorResponseError.TEMPORARILY_UNAVAILABLE:
            return temporarily_unavailable()
        if self is OAuth2ErrorResponseError.INVALID_CLIENT:
            return invalid_client()
        if self is OAuth2ErrorResponseError.INVALID_GRANT:
            return invalid_grant()
        if self is OAuth2ErrorResponseError.UNSUPPORTED_GRANT_TYPE:
            return unsupported_grant_type()
