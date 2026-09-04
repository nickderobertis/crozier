

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostAuthorizationLinkAuthResponseErrorsItemErrorCode(enum.StrEnum):
    INVALID_TRANSACTION = "invalid_transaction"
    INVALID_TRANSACTION_ID = "invalid_transaction_id"
    INVALID_LINK_CODE = "invalid_link_code"
    RESPONSE_TIMEOUT = "response_timeout"
    UNKNOWN_ERROR = "unknown_error"

    def visit(
        self,
        invalid_transaction: typing.Callable[[], T_Result],
        invalid_transaction_id: typing.Callable[[], T_Result],
        invalid_link_code: typing.Callable[[], T_Result],
        response_timeout: typing.Callable[[], T_Result],
        unknown_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostAuthorizationLinkAuthResponseErrorsItemErrorCode.INVALID_TRANSACTION:
            return invalid_transaction()
        if self is PostAuthorizationLinkAuthResponseErrorsItemErrorCode.INVALID_TRANSACTION_ID:
            return invalid_transaction_id()
        if self is PostAuthorizationLinkAuthResponseErrorsItemErrorCode.INVALID_LINK_CODE:
            return invalid_link_code()
        if self is PostAuthorizationLinkAuthResponseErrorsItemErrorCode.RESPONSE_TIMEOUT:
            return response_timeout()
        if self is PostAuthorizationLinkAuthResponseErrorsItemErrorCode.UNKNOWN_ERROR:
            return unknown_error()
