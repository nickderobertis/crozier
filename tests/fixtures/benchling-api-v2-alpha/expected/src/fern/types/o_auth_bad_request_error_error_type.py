

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OAuthBadRequestErrorErrorType(enum.StrEnum):
    INVALID_REQUEST = "invalid_request"
    INVALID_GRANT = "invalid_grant"
    UNAUTHORIZED_CLIENT = "unauthorized_client"
    UNSUPPORTED_GRANT_TYPE = "unsupported_grant_type"

    def visit(
        self,
        invalid_request: typing.Callable[[], T_Result],
        invalid_grant: typing.Callable[[], T_Result],
        unauthorized_client: typing.Callable[[], T_Result],
        unsupported_grant_type: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OAuthBadRequestErrorErrorType.INVALID_REQUEST:
            return invalid_request()
        if self is OAuthBadRequestErrorErrorType.INVALID_GRANT:
            return invalid_grant()
        if self is OAuthBadRequestErrorErrorType.UNAUTHORIZED_CLIENT:
            return unauthorized_client()
        if self is OAuthBadRequestErrorErrorType.UNSUPPORTED_GRANT_TYPE:
            return unsupported_grant_type()
