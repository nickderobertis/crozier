

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostLinkedAuthenticateResponseErrorsItemErrorCode(enum.StrEnum):
    INVALID_TRANSACTION_ID = "invalid_transaction_id"
    INVALID_TRANSACTION = "invalid_transaction"
    INVALID_IDENTIFIER = "invalid_identifier"
    INVALID_NO_OF_CHALLENGES = "invalid_no_of_challenges"
    AUTH_FAILED = "auth_failed"
    UNKNOWN_ERROR = "unknown_error"
    INVALID_AUTH_FACTOR_TYPE_FORMAT = "invalid_auth_factor_type_format"
    INVALID_AUTH_FACTOR_TYPE = "invalid_auth_factor_type"
    INVALID_CHALLENGE = "invalid_challenge"
    INVALID_CHALLENGE_LENGTH = "invalid_challenge_length"
    INVALID_CHALLENGE_FORMAT = "invalid_challenge_format"

    def visit(
        self,
        invalid_transaction_id: typing.Callable[[], T_Result],
        invalid_transaction: typing.Callable[[], T_Result],
        invalid_identifier: typing.Callable[[], T_Result],
        invalid_no_of_challenges: typing.Callable[[], T_Result],
        auth_failed: typing.Callable[[], T_Result],
        unknown_error: typing.Callable[[], T_Result],
        invalid_auth_factor_type_format: typing.Callable[[], T_Result],
        invalid_auth_factor_type: typing.Callable[[], T_Result],
        invalid_challenge: typing.Callable[[], T_Result],
        invalid_challenge_length: typing.Callable[[], T_Result],
        invalid_challenge_format: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostLinkedAuthenticateResponseErrorsItemErrorCode.INVALID_TRANSACTION_ID:
            return invalid_transaction_id()
        if self is PostLinkedAuthenticateResponseErrorsItemErrorCode.INVALID_TRANSACTION:
            return invalid_transaction()
        if self is PostLinkedAuthenticateResponseErrorsItemErrorCode.INVALID_IDENTIFIER:
            return invalid_identifier()
        if self is PostLinkedAuthenticateResponseErrorsItemErrorCode.INVALID_NO_OF_CHALLENGES:
            return invalid_no_of_challenges()
        if self is PostLinkedAuthenticateResponseErrorsItemErrorCode.AUTH_FAILED:
            return auth_failed()
        if self is PostLinkedAuthenticateResponseErrorsItemErrorCode.UNKNOWN_ERROR:
            return unknown_error()
        if self is PostLinkedAuthenticateResponseErrorsItemErrorCode.INVALID_AUTH_FACTOR_TYPE_FORMAT:
            return invalid_auth_factor_type_format()
        if self is PostLinkedAuthenticateResponseErrorsItemErrorCode.INVALID_AUTH_FACTOR_TYPE:
            return invalid_auth_factor_type()
        if self is PostLinkedAuthenticateResponseErrorsItemErrorCode.INVALID_CHALLENGE:
            return invalid_challenge()
        if self is PostLinkedAuthenticateResponseErrorsItemErrorCode.INVALID_CHALLENGE_LENGTH:
            return invalid_challenge_length()
        if self is PostLinkedAuthenticateResponseErrorsItemErrorCode.INVALID_CHALLENGE_FORMAT:
            return invalid_challenge_format()
