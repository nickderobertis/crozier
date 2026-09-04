

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostAuthorizationLinkTransactionResponseErrorsItemErrorCode(enum.StrEnum):
    INVALID_LINK_CODE = "invalid_link_code"
    INVALID_TRANSACTION = "invalid_transaction"
    INVALID_CLIENT_ID = "invalid_client_id"
    UNKNOWN_ERROR = "unknown_error"

    def visit(
        self,
        invalid_link_code: typing.Callable[[], T_Result],
        invalid_transaction: typing.Callable[[], T_Result],
        invalid_client_id: typing.Callable[[], T_Result],
        unknown_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostAuthorizationLinkTransactionResponseErrorsItemErrorCode.INVALID_LINK_CODE:
            return invalid_link_code()
        if self is PostAuthorizationLinkTransactionResponseErrorsItemErrorCode.INVALID_TRANSACTION:
            return invalid_transaction()
        if self is PostAuthorizationLinkTransactionResponseErrorsItemErrorCode.INVALID_CLIENT_ID:
            return invalid_client_id()
        if self is PostAuthorizationLinkTransactionResponseErrorsItemErrorCode.UNKNOWN_ERROR:
            return unknown_error()
