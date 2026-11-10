

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssetType(enum.StrEnum):
    """
    A value from a MISMO prescribed list that specifies financial assets in a mortgage loan transaction. Assets may be either liquid or fixed and are associated with a corresponding asset amount.
    """

    CHECKING_ACCOUNT = "CheckingAccount"
    SAVINGS_ACCOUNT = "SavingsAccount"
    INVESTMENT = "Investment"
    MONEY_MARKET_FUND = "MoneyMarketFund"
    OTHER = "Other"

    def visit(
        self,
        checking_account: typing.Callable[[], T_Result],
        savings_account: typing.Callable[[], T_Result],
        investment: typing.Callable[[], T_Result],
        money_market_fund: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AssetType.CHECKING_ACCOUNT:
            return checking_account()
        if self is AssetType.SAVINGS_ACCOUNT:
            return savings_account()
        if self is AssetType.INVESTMENT:
            return investment()
        if self is AssetType.MONEY_MARKET_FUND:
            return money_market_fund()
        if self is AssetType.OTHER:
            return other()
