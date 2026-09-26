

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetDataIntegritySummariesRequestDataType(enum.StrEnum):
    BANKING_ACCOUNTS = "banking-accounts"
    BANKING_TRANSACTIONS = "banking-transactions"
    BANK_ACCOUNTS = "bankAccounts"
    ACCOUNT_TRANSACTIONS = "accountTransactions"

    def visit(
        self,
        banking_accounts: typing.Callable[[], T_Result],
        banking_transactions: typing.Callable[[], T_Result],
        bank_accounts: typing.Callable[[], T_Result],
        account_transactions: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetDataIntegritySummariesRequestDataType.BANKING_ACCOUNTS:
            return banking_accounts()
        if self is GetDataIntegritySummariesRequestDataType.BANKING_TRANSACTIONS:
            return banking_transactions()
        if self is GetDataIntegritySummariesRequestDataType.BANK_ACCOUNTS:
            return bank_accounts()
        if self is GetDataIntegritySummariesRequestDataType.ACCOUNT_TRANSACTIONS:
            return account_transactions()
