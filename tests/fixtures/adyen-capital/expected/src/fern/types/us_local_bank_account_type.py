

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UsLocalBankAccountType(enum.StrEnum):
    CHECKING = "checking"
    SAVINGS = "savings"

    def visit(self, checking: typing.Callable[[], T_Result], savings: typing.Callable[[], T_Result]) -> T_Result:
        if self is UsLocalBankAccountType.CHECKING:
            return checking()
        if self is UsLocalBankAccountType.SAVINGS:
            return savings()
