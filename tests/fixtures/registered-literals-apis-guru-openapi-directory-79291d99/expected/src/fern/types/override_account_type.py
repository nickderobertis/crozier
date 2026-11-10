

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OverrideAccountType(enum.StrEnum):
    """
    `investment:` Investment account.

    `credit:` Credit card

    `depository:` Depository account

    `loan:` Loan account

    `payroll:` Payroll account

    `other:` Non-specified account type

    See the [Account type schema](https://plaid.com/docs/api/accounts#account-type-schema) for a full listing of account types and corresponding subtypes.
    """

    INVESTMENT = "investment"
    CREDIT = "credit"
    DEPOSITORY = "depository"
    LOAN = "loan"
    PAYROLL = "payroll"
    OTHER = "other"

    def visit(
        self,
        investment: typing.Callable[[], T_Result],
        credit: typing.Callable[[], T_Result],
        depository: typing.Callable[[], T_Result],
        loan: typing.Callable[[], T_Result],
        payroll: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OverrideAccountType.INVESTMENT:
            return investment()
        if self is OverrideAccountType.CREDIT:
            return credit()
        if self is OverrideAccountType.DEPOSITORY:
            return depository()
        if self is OverrideAccountType.LOAN:
            return loan()
        if self is OverrideAccountType.PAYROLL:
            return payroll()
        if self is OverrideAccountType.OTHER:
            return other()
