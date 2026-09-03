

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostWalletBindingResponseErrorsItemErrorCode(enum.StrEnum):
    KEY_BINDING_FAILED = "key_binding_failed"
    INVALID_PUBLIC_KEY = "invalid_public_key"
    INVALID_AUTH_CHALLENGE = "invalid_auth_challenge"
    DUPLICATE_PUBLIC_KEY = "duplicate_public_key"
    INVALID_AUTH_FACTOR_TYPE_FORMAT = "invalid_auth_factor_type_format"
    INVALID_AUTH_FACTOR_TYPE = "invalid_auth_factor_type"
    INVALID_CHALLENGE = "invalid_challenge"
    INVALID_CHALLENGE_LENGTH = "invalid_challenge_length"
    INVALID_CHALLENGE_FORMAT = "invalid_challenge_format"

    def visit(
        self,
        key_binding_failed: typing.Callable[[], T_Result],
        invalid_public_key: typing.Callable[[], T_Result],
        invalid_auth_challenge: typing.Callable[[], T_Result],
        duplicate_public_key: typing.Callable[[], T_Result],
        invalid_auth_factor_type_format: typing.Callable[[], T_Result],
        invalid_auth_factor_type: typing.Callable[[], T_Result],
        invalid_challenge: typing.Callable[[], T_Result],
        invalid_challenge_length: typing.Callable[[], T_Result],
        invalid_challenge_format: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostWalletBindingResponseErrorsItemErrorCode.KEY_BINDING_FAILED:
            return key_binding_failed()
        if self is PostWalletBindingResponseErrorsItemErrorCode.INVALID_PUBLIC_KEY:
            return invalid_public_key()
        if self is PostWalletBindingResponseErrorsItemErrorCode.INVALID_AUTH_CHALLENGE:
            return invalid_auth_challenge()
        if self is PostWalletBindingResponseErrorsItemErrorCode.DUPLICATE_PUBLIC_KEY:
            return duplicate_public_key()
        if self is PostWalletBindingResponseErrorsItemErrorCode.INVALID_AUTH_FACTOR_TYPE_FORMAT:
            return invalid_auth_factor_type_format()
        if self is PostWalletBindingResponseErrorsItemErrorCode.INVALID_AUTH_FACTOR_TYPE:
            return invalid_auth_factor_type()
        if self is PostWalletBindingResponseErrorsItemErrorCode.INVALID_CHALLENGE:
            return invalid_challenge()
        if self is PostWalletBindingResponseErrorsItemErrorCode.INVALID_CHALLENGE_LENGTH:
            return invalid_challenge_length()
        if self is PostWalletBindingResponseErrorsItemErrorCode.INVALID_CHALLENGE_FORMAT:
            return invalid_challenge_format()
