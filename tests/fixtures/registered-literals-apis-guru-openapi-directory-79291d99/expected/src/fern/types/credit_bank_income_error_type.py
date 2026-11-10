

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreditBankIncomeErrorType(enum.StrEnum):
    """
    A broad categorization of the error. Safe for programmatic use.
    """

    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    INSUFFICIENT_CREDENTIALS = "INSUFFICIENT_CREDENTIALS"
    ITEM_LOCKED = "ITEM_LOCKED"
    USER_SETUP_REQUIRED = "USER_SETUP_REQUIRED"
    COUNTRY_NOT_SUPPORTED = "COUNTRY_NOT_SUPPORTED"
    INSTITUTION_DOWN = "INSTITUTION_DOWN"
    INSTITUTION_NO_LONGER_SUPPORTED = "INSTITUTION_NO_LONGER_SUPPORTED"
    INSTITUTION_NOT_RESPONDING = "INSTITUTION_NOT_RESPONDING"
    INVALID_CREDENTIALS = "INVALID_CREDENTIALS"
    INVALID_MFA = "INVALID_MFA"
    INVALID_SEND_METHOD = "INVALID_SEND_METHOD"
    ITEM_LOGIN_REQUIRED = "ITEM_LOGIN_REQUIRED"
    MFA_NOT_SUPPORTED = "MFA_NOT_SUPPORTED"
    NO_ACCOUNTS = "NO_ACCOUNTS"
    ITEM_NOT_SUPPORTED = "ITEM_NOT_SUPPORTED"
    ACCESS_NOT_GRANTED = "ACCESS_NOT_GRANTED"

    def visit(
        self,
        internal_server_error: typing.Callable[[], T_Result],
        insufficient_credentials: typing.Callable[[], T_Result],
        item_locked: typing.Callable[[], T_Result],
        user_setup_required: typing.Callable[[], T_Result],
        country_not_supported: typing.Callable[[], T_Result],
        institution_down: typing.Callable[[], T_Result],
        institution_no_longer_supported: typing.Callable[[], T_Result],
        institution_not_responding: typing.Callable[[], T_Result],
        invalid_credentials: typing.Callable[[], T_Result],
        invalid_mfa: typing.Callable[[], T_Result],
        invalid_send_method: typing.Callable[[], T_Result],
        item_login_required: typing.Callable[[], T_Result],
        mfa_not_supported: typing.Callable[[], T_Result],
        no_accounts: typing.Callable[[], T_Result],
        item_not_supported: typing.Callable[[], T_Result],
        access_not_granted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreditBankIncomeErrorType.INTERNAL_SERVER_ERROR:
            return internal_server_error()
        if self is CreditBankIncomeErrorType.INSUFFICIENT_CREDENTIALS:
            return insufficient_credentials()
        if self is CreditBankIncomeErrorType.ITEM_LOCKED:
            return item_locked()
        if self is CreditBankIncomeErrorType.USER_SETUP_REQUIRED:
            return user_setup_required()
        if self is CreditBankIncomeErrorType.COUNTRY_NOT_SUPPORTED:
            return country_not_supported()
        if self is CreditBankIncomeErrorType.INSTITUTION_DOWN:
            return institution_down()
        if self is CreditBankIncomeErrorType.INSTITUTION_NO_LONGER_SUPPORTED:
            return institution_no_longer_supported()
        if self is CreditBankIncomeErrorType.INSTITUTION_NOT_RESPONDING:
            return institution_not_responding()
        if self is CreditBankIncomeErrorType.INVALID_CREDENTIALS:
            return invalid_credentials()
        if self is CreditBankIncomeErrorType.INVALID_MFA:
            return invalid_mfa()
        if self is CreditBankIncomeErrorType.INVALID_SEND_METHOD:
            return invalid_send_method()
        if self is CreditBankIncomeErrorType.ITEM_LOGIN_REQUIRED:
            return item_login_required()
        if self is CreditBankIncomeErrorType.MFA_NOT_SUPPORTED:
            return mfa_not_supported()
        if self is CreditBankIncomeErrorType.NO_ACCOUNTS:
            return no_accounts()
        if self is CreditBankIncomeErrorType.ITEM_NOT_SUPPORTED:
            return item_not_supported()
        if self is CreditBankIncomeErrorType.ACCESS_NOT_GRANTED:
            return access_not_granted()
