

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObCreditDebitCode0(str, enum.Enum):
    """
    Indicates whether the amount is a credit or a debit.
    Usage: A zero amount is considered to be a credit amount.
    """

    CREDIT = "Credit"
    DEBIT = "Debit"

    def visit(self, credit: typing.Callable[[], T_Result], debit: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObCreditDebitCode0.CREDIT:
            return credit()
        if self is ObCreditDebitCode0.DEBIT:
            return debit()
