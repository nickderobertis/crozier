

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutOidcClientClientIdResponseErrorsItemErrorCode(enum.StrEnum):
    INVALID_CLIENT_ID = "invalid_client_id"
    INVALID_CLIENT_NAME = "invalid_client_name"
    INVALID_CLAIM = "invalid_claim"
    INVALID_ACR = "invalid_acr"
    INVALID_URI = "invalid_uri"
    INVALID_REDIRECT_URI = "invalid_redirect_uri"
    INVALID_GRANT_TYPE = "invalid_grant_type"
    INVALID_CLIENT_AUTH = "invalid_client_auth"

    def visit(
        self,
        invalid_client_id: typing.Callable[[], T_Result],
        invalid_client_name: typing.Callable[[], T_Result],
        invalid_claim: typing.Callable[[], T_Result],
        invalid_acr: typing.Callable[[], T_Result],
        invalid_uri: typing.Callable[[], T_Result],
        invalid_redirect_uri: typing.Callable[[], T_Result],
        invalid_grant_type: typing.Callable[[], T_Result],
        invalid_client_auth: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PutOidcClientClientIdResponseErrorsItemErrorCode.INVALID_CLIENT_ID:
            return invalid_client_id()
        if self is PutOidcClientClientIdResponseErrorsItemErrorCode.INVALID_CLIENT_NAME:
            return invalid_client_name()
        if self is PutOidcClientClientIdResponseErrorsItemErrorCode.INVALID_CLAIM:
            return invalid_claim()
        if self is PutOidcClientClientIdResponseErrorsItemErrorCode.INVALID_ACR:
            return invalid_acr()
        if self is PutOidcClientClientIdResponseErrorsItemErrorCode.INVALID_URI:
            return invalid_uri()
        if self is PutOidcClientClientIdResponseErrorsItemErrorCode.INVALID_REDIRECT_URI:
            return invalid_redirect_uri()
        if self is PutOidcClientClientIdResponseErrorsItemErrorCode.INVALID_GRANT_TYPE:
            return invalid_grant_type()
        if self is PutOidcClientClientIdResponseErrorsItemErrorCode.INVALID_CLIENT_AUTH:
            return invalid_client_auth()
