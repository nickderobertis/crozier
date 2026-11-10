

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreditBankEmploymentWarningType(enum.StrEnum):
    """
    The warning type which will always be `BANK_EMPLOYMENT_WARNING`.
    """

    BANK_EMPLOYMENT_WARNING = "BANK_EMPLOYMENT_WARNING"

    def visit(self, bank_employment_warning: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreditBankEmploymentWarningType.BANK_EMPLOYMENT_WARNING:
            return bank_employment_warning()
