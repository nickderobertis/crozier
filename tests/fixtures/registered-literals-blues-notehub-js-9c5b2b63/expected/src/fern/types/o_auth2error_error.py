

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OAuth2ErrorError(enum.StrEnum):
    """
    RFC 6749 error code.
    """

    INVALID_REQUEST = "invalid_request"
    INVALID_CLIENT = "invalid_client"
    INVALID_GRANT = "invalid_grant"
    UNAUTHORIZED_CLIENT = "unauthorized_client"
    UNSUPPORTED_GRANT_TYPE = "unsupported_grant_type"
    INVALID_SCOPE = "invalid_scope"

    def visit(
        self,
        invalid_request: typing.Callable[[], T_Result],
        invalid_client: typing.Callable[[], T_Result],
        invalid_grant: typing.Callable[[], T_Result],
        unauthorized_client: typing.Callable[[], T_Result],
        unsupported_grant_type: typing.Callable[[], T_Result],
        invalid_scope: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OAuth2ErrorError.INVALID_REQUEST:
            return invalid_request()
        if self is OAuth2ErrorError.INVALID_CLIENT:
            return invalid_client()
        if self is OAuth2ErrorError.INVALID_GRANT:
            return invalid_grant()
        if self is OAuth2ErrorError.UNAUTHORIZED_CLIENT:
            return unauthorized_client()
        if self is OAuth2ErrorError.UNSUPPORTED_GRANT_TYPE:
            return unsupported_grant_type()
        if self is OAuth2ErrorError.INVALID_SCOPE:
            return invalid_scope()
