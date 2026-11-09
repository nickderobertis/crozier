

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InvestmentTransactionType(enum.StrEnum):
    """
    Value is one of the following:
    `buy`: Buying an investment
    `sell`: Selling an investment
    `cancel`: A cancellation of a pending transaction
    `cash`: Activity that modifies a cash position
    `fee`: A fee on the account
    `transfer`: Activity which modifies a position, but not through buy/sell activity e.g. options exercise, portfolio transfer

    For descriptions of possible transaction types and subtypes, see the [Investment transaction types schema](https://plaid.com/docs/api/accounts/#investment-transaction-types-schema).
    """

    BUY = "buy"
    SELL = "sell"
    CANCEL = "cancel"
    CASH = "cash"
    FEE = "fee"
    TRANSFER = "transfer"

    def visit(
        self,
        buy: typing.Callable[[], T_Result],
        sell: typing.Callable[[], T_Result],
        cancel: typing.Callable[[], T_Result],
        cash: typing.Callable[[], T_Result],
        fee: typing.Callable[[], T_Result],
        transfer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvestmentTransactionType.BUY:
            return buy()
        if self is InvestmentTransactionType.SELL:
            return sell()
        if self is InvestmentTransactionType.CANCEL:
            return cancel()
        if self is InvestmentTransactionType.CASH:
            return cash()
        if self is InvestmentTransactionType.FEE:
            return fee()
        if self is InvestmentTransactionType.TRANSFER:
            return transfer()
