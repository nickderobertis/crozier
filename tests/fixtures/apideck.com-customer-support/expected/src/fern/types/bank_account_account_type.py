

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BankAccountAccountType(str, enum.Enum):
    """
    The type of bank account.
    """

    BANK_ACCOUNT = "bank_account"
    CREDIT_CARD = "credit_card"
    OTHER = "other"

    def visit(
        self,
        bank_account: typing.Callable[[], T_Result],
        credit_card: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BankAccountAccountType.BANK_ACCOUNT:
            return bank_account()
        if self is BankAccountAccountType.CREDIT_CARD:
            return credit_card()
        if self is BankAccountAccountType.OTHER:
            return other()
