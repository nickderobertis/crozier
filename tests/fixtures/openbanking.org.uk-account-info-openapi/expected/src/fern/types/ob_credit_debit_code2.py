

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObCreditDebitCode2(str, enum.Enum):
    """
    Indicates whether the balance is a credit or a debit balance.
    Usage: A zero balance is considered to be a credit balance.
    """

    CREDIT = "Credit"
    DEBIT = "Debit"

    def visit(self, credit: typing.Callable[[], T_Result], debit: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObCreditDebitCode2.CREDIT:
            return credit()
        if self is ObCreditDebitCode2.DEBIT:
            return debit()
