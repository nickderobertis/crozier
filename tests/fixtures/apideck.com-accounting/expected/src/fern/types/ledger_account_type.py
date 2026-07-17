

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LedgerAccountType(enum.StrEnum):
    """
    The type of account.
    """

    ACCOUNTS_RECEIVABLE = "accounts_receivable"
    REVENUE = "revenue"
    SALES = "sales"
    OTHER_INCOME = "other_income"
    BANK = "bank"
    CURRENT_ASSET = "current_asset"
    FIXED_ASSET = "fixed_asset"
    NON_CURRENT_ASSET = "non_current_asset"
    OTHER_ASSET = "other_asset"
    BALANCESHEET = "balancesheet"
    EQUITY = "equity"
    EXPENSE = "expense"
    OTHER_EXPENSE = "other_expense"
    COSTS_OF_SALES = "costs_of_sales"
    ACCOUNTS_PAYABLE = "accounts_payable"
    CREDIT_CARD = "credit_card"
    CURRENT_LIABILITY = "current_liability"
    NON_CURRENT_LIABILITY = "non_current_liability"
    OTHER_LIABILITY = "other_liability"

    def visit(
        self,
        accounts_receivable: typing.Callable[[], T_Result],
        revenue: typing.Callable[[], T_Result],
        sales: typing.Callable[[], T_Result],
        other_income: typing.Callable[[], T_Result],
        bank: typing.Callable[[], T_Result],
        current_asset: typing.Callable[[], T_Result],
        fixed_asset: typing.Callable[[], T_Result],
        non_current_asset: typing.Callable[[], T_Result],
        other_asset: typing.Callable[[], T_Result],
        balancesheet: typing.Callable[[], T_Result],
        equity: typing.Callable[[], T_Result],
        expense: typing.Callable[[], T_Result],
        other_expense: typing.Callable[[], T_Result],
        costs_of_sales: typing.Callable[[], T_Result],
        accounts_payable: typing.Callable[[], T_Result],
        credit_card: typing.Callable[[], T_Result],
        current_liability: typing.Callable[[], T_Result],
        non_current_liability: typing.Callable[[], T_Result],
        other_liability: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LedgerAccountType.ACCOUNTS_RECEIVABLE:
            return accounts_receivable()
        if self is LedgerAccountType.REVENUE:
            return revenue()
        if self is LedgerAccountType.SALES:
            return sales()
        if self is LedgerAccountType.OTHER_INCOME:
            return other_income()
        if self is LedgerAccountType.BANK:
            return bank()
        if self is LedgerAccountType.CURRENT_ASSET:
            return current_asset()
        if self is LedgerAccountType.FIXED_ASSET:
            return fixed_asset()
        if self is LedgerAccountType.NON_CURRENT_ASSET:
            return non_current_asset()
        if self is LedgerAccountType.OTHER_ASSET:
            return other_asset()
        if self is LedgerAccountType.BALANCESHEET:
            return balancesheet()
        if self is LedgerAccountType.EQUITY:
            return equity()
        if self is LedgerAccountType.EXPENSE:
            return expense()
        if self is LedgerAccountType.OTHER_EXPENSE:
            return other_expense()
        if self is LedgerAccountType.COSTS_OF_SALES:
            return costs_of_sales()
        if self is LedgerAccountType.ACCOUNTS_PAYABLE:
            return accounts_payable()
        if self is LedgerAccountType.CREDIT_CARD:
            return credit_card()
        if self is LedgerAccountType.CURRENT_LIABILITY:
            return current_liability()
        if self is LedgerAccountType.NON_CURRENT_LIABILITY:
            return non_current_liability()
        if self is LedgerAccountType.OTHER_LIABILITY:
            return other_liability()
