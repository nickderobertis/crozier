

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchClientClientIdResponseErrorsItemErrorCode(enum.StrEnum):
    INVALID_CLIENT_ID = "invalid_client_id"
    INVALID_CLIENT_NAME = "invalid_client_name"
    INVALID_CLAIM = "invalid_claim"
    INVALID_ACR = "invalid_acr"
    INVALID_URI = "invalid_uri"
    INVALID_REDIRECT_URI = "invalid_redirect_uri"
    INVALID_GRANT_TYPE = "invalid_grant_type"
    INVALID_CLIENT_AUTH = "invalid_client_auth"
    INVALID_PUBLIC_KEY = "invalid_public_key"
    INVALID_ADDITIONAL_CONFIG = "invalid_additional_config"

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
        invalid_public_key: typing.Callable[[], T_Result],
        invalid_additional_config: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatchClientClientIdResponseErrorsItemErrorCode.INVALID_CLIENT_ID:
            return invalid_client_id()
        if self is PatchClientClientIdResponseErrorsItemErrorCode.INVALID_CLIENT_NAME:
            return invalid_client_name()
        if self is PatchClientClientIdResponseErrorsItemErrorCode.INVALID_CLAIM:
            return invalid_claim()
        if self is PatchClientClientIdResponseErrorsItemErrorCode.INVALID_ACR:
            return invalid_acr()
        if self is PatchClientClientIdResponseErrorsItemErrorCode.INVALID_URI:
            return invalid_uri()
        if self is PatchClientClientIdResponseErrorsItemErrorCode.INVALID_REDIRECT_URI:
            return invalid_redirect_uri()
        if self is PatchClientClientIdResponseErrorsItemErrorCode.INVALID_GRANT_TYPE:
            return invalid_grant_type()
        if self is PatchClientClientIdResponseErrorsItemErrorCode.INVALID_CLIENT_AUTH:
            return invalid_client_auth()
        if self is PatchClientClientIdResponseErrorsItemErrorCode.INVALID_PUBLIC_KEY:
            return invalid_public_key()
        if self is PatchClientClientIdResponseErrorsItemErrorCode.INVALID_ADDITIONAL_CONFIG:
            return invalid_additional_config()
