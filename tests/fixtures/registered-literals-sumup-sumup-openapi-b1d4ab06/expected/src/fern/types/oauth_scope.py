

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    PAYMENTS = "payments"
    """
    Make payments by creating and processing checkouts.
    """

    CHECKOUTS_READ = "checkouts.read"
    """
    View checkouts.
    """

    CHECKOUTS_WRITE = "checkouts.write"
    """
    Create, process, and deactivate checkouts.
    """

    TRANSACTIONS_HISTORY = "transactions.history"
    """
    View transactions and transaction history.
    """

    TRANSACTIONS_READ = "transactions.read"
    """
    View transactions and transaction history.
    """

    REFUNDS_WRITE = "refunds.write"
    """
    Refund transactions.
    """

    RECEIPTS_READ = "receipts.read"
    """
    View receipts.
    """

    USER_PROFILE_READONLY = "user.profile_readonly"
    """
    View user profile details.
    """

    USER_PROFILE = "user.profile"
    """
    View and manage your user profile.
    """

    USER_APP_SETTINGS = "user.app-settings"
    """
    View and manage the SumUp mobile application settings.
    """

    PAYMENT_INSTRUMENTS = "payment_instruments"
    """
    Manage customers and their payment instruments.
    """

    CUSTOMERS_READ = "customers.read"
    """
    View customers and their payment instruments.
    """

    CUSTOMERS_WRITE = "customers.write"
    """
    Create and manage customers and their payment instruments.
    """

    USER_PAYOUT_SETTINGS = "user.payout-settings"
    """
    View and manage your payout settings.
    """

    PAYOUTS_READ = "payouts.read"
    """
    View payouts.
    """

    USER_SUBACCOUNTS = "user.subaccounts"
    """
    View and manage the user profile details of your employees.
    """

    def visit(
        self,
        payments: typing.Callable[[], T_Result],
        checkouts_read: typing.Callable[[], T_Result],
        checkouts_write: typing.Callable[[], T_Result],
        transactions_history: typing.Callable[[], T_Result],
        transactions_read: typing.Callable[[], T_Result],
        refunds_write: typing.Callable[[], T_Result],
        receipts_read: typing.Callable[[], T_Result],
        user_profile_readonly: typing.Callable[[], T_Result],
        user_profile: typing.Callable[[], T_Result],
        user_app_settings: typing.Callable[[], T_Result],
        payment_instruments: typing.Callable[[], T_Result],
        customers_read: typing.Callable[[], T_Result],
        customers_write: typing.Callable[[], T_Result],
        user_payout_settings: typing.Callable[[], T_Result],
        payouts_read: typing.Callable[[], T_Result],
        user_subaccounts: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OauthScope.PAYMENTS:
            return payments()
        if self is OauthScope.CHECKOUTS_READ:
            return checkouts_read()
        if self is OauthScope.CHECKOUTS_WRITE:
            return checkouts_write()
        if self is OauthScope.TRANSACTIONS_HISTORY:
            return transactions_history()
        if self is OauthScope.TRANSACTIONS_READ:
            return transactions_read()
        if self is OauthScope.REFUNDS_WRITE:
            return refunds_write()
        if self is OauthScope.RECEIPTS_READ:
            return receipts_read()
        if self is OauthScope.USER_PROFILE_READONLY:
            return user_profile_readonly()
        if self is OauthScope.USER_PROFILE:
            return user_profile()
        if self is OauthScope.USER_APP_SETTINGS:
            return user_app_settings()
        if self is OauthScope.PAYMENT_INSTRUMENTS:
            return payment_instruments()
        if self is OauthScope.CUSTOMERS_READ:
            return customers_read()
        if self is OauthScope.CUSTOMERS_WRITE:
            return customers_write()
        if self is OauthScope.USER_PAYOUT_SETTINGS:
            return user_payout_settings()
        if self is OauthScope.PAYOUTS_READ:
            return payouts_read()
        if self is OauthScope.USER_SUBACCOUNTS:
            return user_subaccounts()
