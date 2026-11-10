

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreditBankIncomeAccountType(enum.StrEnum):
    """
    The account type. This will always be `depository`.
    """

    DEPOSITORY = "depository"

    def visit(self, depository: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreditBankIncomeAccountType.DEPOSITORY:
            return depository()
