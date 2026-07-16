

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AccountType(str, enum.Enum):
    """
    See Account Types
    """

    BANK = "BANK"
    CURRENT = "CURRENT"
    CURRLIAB = "CURRLIAB"
    DEPRECIATN = "DEPRECIATN"
    DIRECTCOSTS = "DIRECTCOSTS"
    EQUITY = "EQUITY"
    EXPENSE = "EXPENSE"
    FIXED = "FIXED"
    INVENTORY = "INVENTORY"
    LIABILITY = "LIABILITY"
    NONCURRENT = "NONCURRENT"
    OTHERINCOME = "OTHERINCOME"
    OVERHEADS = "OVERHEADS"
    PREPAYMENT = "PREPAYMENT"
    REVENUE = "REVENUE"
    SALES = "SALES"
    TERMLIAB = "TERMLIAB"
    PAYGLIABILITY = "PAYGLIABILITY"
    PAYG = "PAYG"
    SUPERANNUATIONEXPENSE = "SUPERANNUATIONEXPENSE"
    SUPERANNUATIONLIABILITY = "SUPERANNUATIONLIABILITY"
    WAGESEXPENSE = "WAGESEXPENSE"
    WAGESPAYABLELIABILITY = "WAGESPAYABLELIABILITY"

    def visit(
        self,
        bank: typing.Callable[[], T_Result],
        current: typing.Callable[[], T_Result],
        currliab: typing.Callable[[], T_Result],
        depreciatn: typing.Callable[[], T_Result],
        directcosts: typing.Callable[[], T_Result],
        equity: typing.Callable[[], T_Result],
        expense: typing.Callable[[], T_Result],
        fixed: typing.Callable[[], T_Result],
        inventory: typing.Callable[[], T_Result],
        liability: typing.Callable[[], T_Result],
        noncurrent: typing.Callable[[], T_Result],
        otherincome: typing.Callable[[], T_Result],
        overheads: typing.Callable[[], T_Result],
        prepayment: typing.Callable[[], T_Result],
        revenue: typing.Callable[[], T_Result],
        sales: typing.Callable[[], T_Result],
        termliab: typing.Callable[[], T_Result],
        paygliability: typing.Callable[[], T_Result],
        payg: typing.Callable[[], T_Result],
        superannuationexpense: typing.Callable[[], T_Result],
        superannuationliability: typing.Callable[[], T_Result],
        wagesexpense: typing.Callable[[], T_Result],
        wagespayableliability: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccountType.BANK:
            return bank()
        if self is AccountType.CURRENT:
            return current()
        if self is AccountType.CURRLIAB:
            return currliab()
        if self is AccountType.DEPRECIATN:
            return depreciatn()
        if self is AccountType.DIRECTCOSTS:
            return directcosts()
        if self is AccountType.EQUITY:
            return equity()
        if self is AccountType.EXPENSE:
            return expense()
        if self is AccountType.FIXED:
            return fixed()
        if self is AccountType.INVENTORY:
            return inventory()
        if self is AccountType.LIABILITY:
            return liability()
        if self is AccountType.NONCURRENT:
            return noncurrent()
        if self is AccountType.OTHERINCOME:
            return otherincome()
        if self is AccountType.OVERHEADS:
            return overheads()
        if self is AccountType.PREPAYMENT:
            return prepayment()
        if self is AccountType.REVENUE:
            return revenue()
        if self is AccountType.SALES:
            return sales()
        if self is AccountType.TERMLIAB:
            return termliab()
        if self is AccountType.PAYGLIABILITY:
            return paygliability()
        if self is AccountType.PAYG:
            return payg()
        if self is AccountType.SUPERANNUATIONEXPENSE:
            return superannuationexpense()
        if self is AccountType.SUPERANNUATIONLIABILITY:
            return superannuationliability()
        if self is AccountType.WAGESEXPENSE:
            return wagesexpense()
        if self is AccountType.WAGESPAYABLELIABILITY:
            return wagespayableliability()
