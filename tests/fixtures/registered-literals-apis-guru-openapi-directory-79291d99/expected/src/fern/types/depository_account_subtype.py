

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DepositoryAccountSubtype(enum.StrEnum):
    """
    Valid account subtypes for depository accounts. For a list containing descriptions of each subtype, see [Account schemas](https://plaid.com/docs/api/accounts/#StandaloneAccountType-depository).
    """

    CHECKING = "checking"
    SAVINGS = "savings"
    HSA = "hsa"
    CD = "cd"
    MONEY_MARKET = "money market"
    PAYPAL = "paypal"
    PREPAID = "prepaid"
    CASH_MANAGEMENT = "cash management"
    EBT = "ebt"
    ALL = "all"

    def visit(
        self,
        checking: typing.Callable[[], T_Result],
        savings: typing.Callable[[], T_Result],
        hsa: typing.Callable[[], T_Result],
        cd: typing.Callable[[], T_Result],
        money_market: typing.Callable[[], T_Result],
        paypal: typing.Callable[[], T_Result],
        prepaid: typing.Callable[[], T_Result],
        cash_management: typing.Callable[[], T_Result],
        ebt: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DepositoryAccountSubtype.CHECKING:
            return checking()
        if self is DepositoryAccountSubtype.SAVINGS:
            return savings()
        if self is DepositoryAccountSubtype.HSA:
            return hsa()
        if self is DepositoryAccountSubtype.CD:
            return cd()
        if self is DepositoryAccountSubtype.MONEY_MARKET:
            return money_market()
        if self is DepositoryAccountSubtype.PAYPAL:
            return paypal()
        if self is DepositoryAccountSubtype.PREPAID:
            return prepaid()
        if self is DepositoryAccountSubtype.CASH_MANAGEMENT:
            return cash_management()
        if self is DepositoryAccountSubtype.EBT:
            return ebt()
        if self is DepositoryAccountSubtype.ALL:
            return all_()
