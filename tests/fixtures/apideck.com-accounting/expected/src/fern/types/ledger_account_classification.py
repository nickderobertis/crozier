

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class LedgerAccountClassification(str, enum.Enum):
    """
    The classification of account.
    """

    ASSET = "asset"
    EQUITY = "equity"
    EXPENSE = "expense"
    LIABILITY = "liability"
    REVENUE = "revenue"
    INCOME = "income"
    OTHER_INCOME = "other_income"
    OTHER_EXPENSE = "other_expense"
    COSTS_OF_SALES = "costs_of_sales"

    def visit(
        self,
        asset: typing.Callable[[], T_Result],
        equity: typing.Callable[[], T_Result],
        expense: typing.Callable[[], T_Result],
        liability: typing.Callable[[], T_Result],
        revenue: typing.Callable[[], T_Result],
        income: typing.Callable[[], T_Result],
        other_income: typing.Callable[[], T_Result],
        other_expense: typing.Callable[[], T_Result],
        costs_of_sales: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LedgerAccountClassification.ASSET:
            return asset()
        if self is LedgerAccountClassification.EQUITY:
            return equity()
        if self is LedgerAccountClassification.EXPENSE:
            return expense()
        if self is LedgerAccountClassification.LIABILITY:
            return liability()
        if self is LedgerAccountClassification.REVENUE:
            return revenue()
        if self is LedgerAccountClassification.INCOME:
            return income()
        if self is LedgerAccountClassification.OTHER_INCOME:
            return other_income()
        if self is LedgerAccountClassification.OTHER_EXPENSE:
            return other_expense()
        if self is LedgerAccountClassification.COSTS_OF_SALES:
            return costs_of_sales()
