

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetConsentDetailsResponseErrorsItemErrorCode(enum.StrEnum):
    INVALID_TRANSACTION = "invalid_transaction"
    UNKNOWN_ERROR = "unknown_error"
    INVALID_REQUEST = "invalid_request"

    def visit(
        self,
        invalid_transaction: typing.Callable[[], T_Result],
        unknown_error: typing.Callable[[], T_Result],
        invalid_request: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetConsentDetailsResponseErrorsItemErrorCode.INVALID_TRANSACTION:
            return invalid_transaction()
        if self is GetConsentDetailsResponseErrorsItemErrorCode.UNKNOWN_ERROR:
            return unknown_error()
        if self is GetConsentDetailsResponseErrorsItemErrorCode.INVALID_REQUEST:
            return invalid_request()
