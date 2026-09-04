

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CaLocalBankAccountType(enum.StrEnum):
    CHECKING = "checking"
    SAVINGS = "savings"

    def visit(self, checking: typing.Callable[[], T_Result], savings: typing.Callable[[], T_Result]) -> T_Result:
        if self is CaLocalBankAccountType.CHECKING:
            return checking()
        if self is CaLocalBankAccountType.SAVINGS:
            return savings()
