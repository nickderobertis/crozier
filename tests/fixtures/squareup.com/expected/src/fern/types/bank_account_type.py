

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BankAccountType(enum.StrEnum):
    """
    Indicates the financial purpose of the bank account.
    """

    CHECKING = "CHECKING"
    SAVINGS = "SAVINGS"
    INVESTMENT = "INVESTMENT"
    OTHER = "OTHER"
    BUSINESS_CHECKING = "BUSINESS_CHECKING"

    def visit(
        self,
        checking: typing.Callable[[], T_Result],
        savings: typing.Callable[[], T_Result],
        investment: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        business_checking: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BankAccountType.CHECKING:
            return checking()
        if self is BankAccountType.SAVINGS:
            return savings()
        if self is BankAccountType.INVESTMENT:
            return investment()
        if self is BankAccountType.OTHER:
            return other()
        if self is BankAccountType.BUSINESS_CHECKING:
            return business_checking()
