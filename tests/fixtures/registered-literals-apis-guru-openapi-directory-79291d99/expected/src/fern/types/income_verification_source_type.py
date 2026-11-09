

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IncomeVerificationSourceType(enum.StrEnum):
    """
    The types of source income data that users should be able to share
    """

    BANK = "bank"
    PAYROLL = "payroll"

    def visit(self, bank: typing.Callable[[], T_Result], payroll: typing.Callable[[], T_Result]) -> T_Result:
        if self is IncomeVerificationSourceType.BANK:
            return bank()
        if self is IncomeVerificationSourceType.PAYROLL:
            return payroll()
