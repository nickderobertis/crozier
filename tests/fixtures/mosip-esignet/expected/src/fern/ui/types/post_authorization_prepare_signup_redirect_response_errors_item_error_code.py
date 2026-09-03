

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostAuthorizationPrepareSignupRedirectResponseErrorsItemErrorCode(enum.StrEnum):
    INVALID_TRANSACTION = "invalid_transaction"
    UNKNOWN_ERROR = "unknown_error"
    INVALID_REQUEST = "invalid_request"
    INVALID_TRANSACTION_ID = "invalid_transaction_id"

    def visit(
        self,
        invalid_transaction: typing.Callable[[], T_Result],
        unknown_error: typing.Callable[[], T_Result],
        invalid_request: typing.Callable[[], T_Result],
        invalid_transaction_id: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostAuthorizationPrepareSignupRedirectResponseErrorsItemErrorCode.INVALID_TRANSACTION:
            return invalid_transaction()
        if self is PostAuthorizationPrepareSignupRedirectResponseErrorsItemErrorCode.UNKNOWN_ERROR:
            return unknown_error()
        if self is PostAuthorizationPrepareSignupRedirectResponseErrorsItemErrorCode.INVALID_REQUEST:
            return invalid_request()
        if self is PostAuthorizationPrepareSignupRedirectResponseErrorsItemErrorCode.INVALID_TRANSACTION_ID:
            return invalid_transaction_id()
