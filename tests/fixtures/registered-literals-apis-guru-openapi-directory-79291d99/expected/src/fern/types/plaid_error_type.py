

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlaidErrorType(enum.StrEnum):
    """
    A broad categorization of the error. Safe for programmatic use.
    """

    INVALID_REQUEST = "INVALID_REQUEST"
    INVALID_RESULT = "INVALID_RESULT"
    INVALID_INPUT = "INVALID_INPUT"
    INSTITUTION_ERROR = "INSTITUTION_ERROR"
    RATE_LIMIT_EXCEEDED = "RATE_LIMIT_EXCEEDED"
    API_ERROR = "API_ERROR"
    ITEM_ERROR = "ITEM_ERROR"
    ASSET_REPORT_ERROR = "ASSET_REPORT_ERROR"
    RECAPTCHA_ERROR = "RECAPTCHA_ERROR"
    OAUTH_ERROR = "OAUTH_ERROR"
    PAYMENT_ERROR = "PAYMENT_ERROR"
    BANK_TRANSFER_ERROR = "BANK_TRANSFER_ERROR"
    INCOME_VERIFICATION_ERROR = "INCOME_VERIFICATION_ERROR"
    MICRODEPOSITS_ERROR = "MICRODEPOSITS_ERROR"

    def visit(
        self,
        invalid_request: typing.Callable[[], T_Result],
        invalid_result: typing.Callable[[], T_Result],
        invalid_input: typing.Callable[[], T_Result],
        institution_error: typing.Callable[[], T_Result],
        rate_limit_exceeded: typing.Callable[[], T_Result],
        api_error: typing.Callable[[], T_Result],
        item_error: typing.Callable[[], T_Result],
        asset_report_error: typing.Callable[[], T_Result],
        recaptcha_error: typing.Callable[[], T_Result],
        oauth_error: typing.Callable[[], T_Result],
        payment_error: typing.Callable[[], T_Result],
        bank_transfer_error: typing.Callable[[], T_Result],
        income_verification_error: typing.Callable[[], T_Result],
        microdeposits_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PlaidErrorType.INVALID_REQUEST:
            return invalid_request()
        if self is PlaidErrorType.INVALID_RESULT:
            return invalid_result()
        if self is PlaidErrorType.INVALID_INPUT:
            return invalid_input()
        if self is PlaidErrorType.INSTITUTION_ERROR:
            return institution_error()
        if self is PlaidErrorType.RATE_LIMIT_EXCEEDED:
            return rate_limit_exceeded()
        if self is PlaidErrorType.API_ERROR:
            return api_error()
        if self is PlaidErrorType.ITEM_ERROR:
            return item_error()
        if self is PlaidErrorType.ASSET_REPORT_ERROR:
            return asset_report_error()
        if self is PlaidErrorType.RECAPTCHA_ERROR:
            return recaptcha_error()
        if self is PlaidErrorType.OAUTH_ERROR:
            return oauth_error()
        if self is PlaidErrorType.PAYMENT_ERROR:
            return payment_error()
        if self is PlaidErrorType.BANK_TRANSFER_ERROR:
            return bank_transfer_error()
        if self is PlaidErrorType.INCOME_VERIFICATION_ERROR:
            return income_verification_error()
        if self is PlaidErrorType.MICRODEPOSITS_ERROR:
            return microdeposits_error()
