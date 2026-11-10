

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreditSessionBankIncomeStatus(enum.StrEnum):
    """
    The terminal status of the bank income verification.

    `APPROVED`: User has approved and verified their income

    `NO_DEPOSITS_FOUND`: We attempted, but were unable to find any income in the connected account.

    `USER_REPORTED_NO_INCOME`: The user explicitly indicated that they don't receive income in the connected account.
    """

    APPROVED = "APPROVED"
    NO_DEPOSITS_FOUND = "NO_DEPOSITS_FOUND"
    USER_REPORTED_NO_INCOME = "USER_REPORTED_NO_INCOME"

    def visit(
        self,
        approved: typing.Callable[[], T_Result],
        no_deposits_found: typing.Callable[[], T_Result],
        user_reported_no_income: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreditSessionBankIncomeStatus.APPROVED:
            return approved()
        if self is CreditSessionBankIncomeStatus.NO_DEPOSITS_FOUND:
            return no_deposits_found()
        if self is CreditSessionBankIncomeStatus.USER_REPORTED_NO_INCOME:
            return user_reported_no_income()
