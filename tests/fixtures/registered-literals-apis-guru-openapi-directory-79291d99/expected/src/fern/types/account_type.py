

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccountType(enum.StrEnum):
    """
    `investment:` Investment account. In API versions 2018-05-22 and earlier, this type is called `brokerage` instead.

    `credit:` Credit card

    `depository:` Depository account

    `loan:` Loan account

    `other:` Non-specified account type

    See the [Account type schema](https://plaid.com/docs/api/accounts#account-type-schema) for a full listing of account types and corresponding subtypes.
    """

    INVESTMENT = "investment"
    CREDIT = "credit"
    DEPOSITORY = "depository"
    LOAN = "loan"
    BROKERAGE = "brokerage"
    OTHER = "other"

    def visit(
        self,
        investment: typing.Callable[[], T_Result],
        credit: typing.Callable[[], T_Result],
        depository: typing.Callable[[], T_Result],
        loan: typing.Callable[[], T_Result],
        brokerage: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccountType.INVESTMENT:
            return investment()
        if self is AccountType.CREDIT:
            return credit()
        if self is AccountType.DEPOSITORY:
            return depository()
        if self is AccountType.LOAN:
            return loan()
        if self is AccountType.BROKERAGE:
            return brokerage()
        if self is AccountType.OTHER:
            return other()
