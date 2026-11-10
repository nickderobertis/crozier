

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreditBankIncomeWarningCode(enum.StrEnum):
    """
    The warning code identifies a specific kind of warning.
    `IDENTITY_UNAVAILABLE`: Unable to extract identity for the Item
    `TRANSACTIONS_UNAVAILABLE`: Unable to extract transactions for the Item
    `ITEM_UNAPPROVED`: User exited flow before giving permission to share data for the Item
    `REPORT_DELETED`: Report deleted due to customer or consumer request
    `DATA_UNAVAILABLE`: No relevant data was found for the Item
    """

    IDENTITY_UNAVAILABLE = "IDENTITY_UNAVAILABLE"
    TRANSACTIONS_UNAVAILABLE = "TRANSACTIONS_UNAVAILABLE"
    ITEM_UNAPPROVED = "ITEM_UNAPPROVED"
    REPORT_DELETED = "REPORT_DELETED"
    DATA_UNAVAILABLE = "DATA_UNAVAILABLE"

    def visit(
        self,
        identity_unavailable: typing.Callable[[], T_Result],
        transactions_unavailable: typing.Callable[[], T_Result],
        item_unapproved: typing.Callable[[], T_Result],
        report_deleted: typing.Callable[[], T_Result],
        data_unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreditBankIncomeWarningCode.IDENTITY_UNAVAILABLE:
            return identity_unavailable()
        if self is CreditBankIncomeWarningCode.TRANSACTIONS_UNAVAILABLE:
            return transactions_unavailable()
        if self is CreditBankIncomeWarningCode.ITEM_UNAPPROVED:
            return item_unapproved()
        if self is CreditBankIncomeWarningCode.REPORT_DELETED:
            return report_deleted()
        if self is CreditBankIncomeWarningCode.DATA_UNAVAILABLE:
            return data_unavailable()
