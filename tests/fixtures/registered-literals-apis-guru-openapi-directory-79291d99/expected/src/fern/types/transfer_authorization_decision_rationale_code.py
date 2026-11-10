

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferAuthorizationDecisionRationaleCode(enum.StrEnum):
    """
    A code representing the rationale for approving or declining the proposed transfer. Possible values are:

    `MANUALLY_VERIFIED_ITEM` – Item created via same-day micro deposits, limited information available. Plaid will offer `approved` as a transaction decision.

    `ITEM_LOGIN_REQUIRED` – Unable to collect the account information due to Item staleness. Can be rectified using Link in update mode. Plaid will offer `approved` as a transaction decision.

    `PAYMENT_PROFILE_LOGIN_REQUIRED` - Unable to collect the account information due to invalid login when using Payment Profiles. Can be rectified using update mode for Payment Profile. Plaid will offer `approved` as a transaction decision.

    `ERROR` – Unable to collect the account information due to an error. Plaid will offer `approved` as a transaction decision.

    `NSF` – Transaction likely to result in a return due to insufficient funds. Plaid will offer `declined` as a transaction decision.

    `RISK` - Transaction is high-risk. Plaid will offer `declined` as a transaction decision.

    `TRANSFER_LIMIT_REACHED` - One or several transfer limits are reached, e.g. monthly transfer limit. Plaid will offer `declined` as a transaction decision.

    `MIGRATED_ACCOUNT_ITEM` - Item created via `/transfer/account_migration` endpoint, limited information available. Plaid will offer `approved` as a transaction decision.
    """

    NSF = "NSF"
    RISK = "RISK"
    TRANSFER_LIMIT_REACHED = "TRANSFER_LIMIT_REACHED"
    MANUALLY_VERIFIED_ITEM = "MANUALLY_VERIFIED_ITEM"
    ITEM_LOGIN_REQUIRED = "ITEM_LOGIN_REQUIRED"
    PAYMENT_PROFILE_LOGIN_REQUIRED = "PAYMENT_PROFILE_LOGIN_REQUIRED"
    ERROR = "ERROR"
    MIGRATED_ACCOUNT_ITEM = "MIGRATED_ACCOUNT_ITEM"

    def visit(
        self,
        nsf: typing.Callable[[], T_Result],
        risk: typing.Callable[[], T_Result],
        transfer_limit_reached: typing.Callable[[], T_Result],
        manually_verified_item: typing.Callable[[], T_Result],
        item_login_required: typing.Callable[[], T_Result],
        payment_profile_login_required: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        migrated_account_item: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransferAuthorizationDecisionRationaleCode.NSF:
            return nsf()
        if self is TransferAuthorizationDecisionRationaleCode.RISK:
            return risk()
        if self is TransferAuthorizationDecisionRationaleCode.TRANSFER_LIMIT_REACHED:
            return transfer_limit_reached()
        if self is TransferAuthorizationDecisionRationaleCode.MANUALLY_VERIFIED_ITEM:
            return manually_verified_item()
        if self is TransferAuthorizationDecisionRationaleCode.ITEM_LOGIN_REQUIRED:
            return item_login_required()
        if self is TransferAuthorizationDecisionRationaleCode.PAYMENT_PROFILE_LOGIN_REQUIRED:
            return payment_profile_login_required()
        if self is TransferAuthorizationDecisionRationaleCode.ERROR:
            return error()
        if self is TransferAuthorizationDecisionRationaleCode.MIGRATED_ACCOUNT_ITEM:
            return migrated_account_item()
