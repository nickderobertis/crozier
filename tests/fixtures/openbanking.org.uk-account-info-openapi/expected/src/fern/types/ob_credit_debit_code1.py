

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObCreditDebitCode1(str, enum.Enum):
    """
    Indicates whether the transaction is a credit or a debit entry.
    """

    CREDIT = "Credit"
    DEBIT = "Debit"

    def visit(self, credit: typing.Callable[[], T_Result], debit: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObCreditDebitCode1.CREDIT:
            return credit()
        if self is ObCreditDebitCode1.DEBIT:
            return debit()
