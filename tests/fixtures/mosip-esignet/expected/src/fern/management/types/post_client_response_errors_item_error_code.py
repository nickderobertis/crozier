

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostClientResponseErrorsItemErrorCode(enum.StrEnum):
    DUPLICATE_CLIENT_ID = "duplicate_client_id"
    INVALID_PUBLIC_KEY = "invalid_public_key"
    INVALID_INPUT = "invalid_input"
    INVALID_CLIENT_ID = "invalid_client_id"
    INVALID_CLIENT_NAME = "invalid_client_name"
    INVALID_RP_ID = "invalid_rp_id"
    INVALID_CLAIM = "invalid_claim"
    INVALID_ACR = "invalid_acr"
    INVALID_URI = "invalid_uri"
    INVALID_REDIRECT_URI = "invalid_redirect_uri"
    INVALID_GRANT_TYPE = "invalid_grant_type"
    INVALID_CLIENT_AUTH = "invalid_client_auth"

    def visit(
        self,
        duplicate_client_id: typing.Callable[[], T_Result],
        invalid_public_key: typing.Callable[[], T_Result],
        invalid_input: typing.Callable[[], T_Result],
        invalid_client_id: typing.Callable[[], T_Result],
        invalid_client_name: typing.Callable[[], T_Result],
        invalid_rp_id: typing.Callable[[], T_Result],
        invalid_claim: typing.Callable[[], T_Result],
        invalid_acr: typing.Callable[[], T_Result],
        invalid_uri: typing.Callable[[], T_Result],
        invalid_redirect_uri: typing.Callable[[], T_Result],
        invalid_grant_type: typing.Callable[[], T_Result],
        invalid_client_auth: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostClientResponseErrorsItemErrorCode.DUPLICATE_CLIENT_ID:
            return duplicate_client_id()
        if self is PostClientResponseErrorsItemErrorCode.INVALID_PUBLIC_KEY:
            return invalid_public_key()
        if self is PostClientResponseErrorsItemErrorCode.INVALID_INPUT:
            return invalid_input()
        if self is PostClientResponseErrorsItemErrorCode.INVALID_CLIENT_ID:
            return invalid_client_id()
        if self is PostClientResponseErrorsItemErrorCode.INVALID_CLIENT_NAME:
            return invalid_client_name()
        if self is PostClientResponseErrorsItemErrorCode.INVALID_RP_ID:
            return invalid_rp_id()
        if self is PostClientResponseErrorsItemErrorCode.INVALID_CLAIM:
            return invalid_claim()
        if self is PostClientResponseErrorsItemErrorCode.INVALID_ACR:
            return invalid_acr()
        if self is PostClientResponseErrorsItemErrorCode.INVALID_URI:
            return invalid_uri()
        if self is PostClientResponseErrorsItemErrorCode.INVALID_REDIRECT_URI:
            return invalid_redirect_uri()
        if self is PostClientResponseErrorsItemErrorCode.INVALID_GRANT_TYPE:
            return invalid_grant_type()
        if self is PostClientResponseErrorsItemErrorCode.INVALID_CLIENT_AUTH:
            return invalid_client_auth()
