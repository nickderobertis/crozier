

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreditBankIncomeWarningType(enum.StrEnum):
    """
    The warning type which will always be `BANK_INCOME_WARNING`.
    """

    BANK_INCOME_WARNING = "BANK_INCOME_WARNING"

    def visit(self, bank_income_warning: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreditBankIncomeWarningType.BANK_INCOME_WARNING:
            return bank_income_warning()
