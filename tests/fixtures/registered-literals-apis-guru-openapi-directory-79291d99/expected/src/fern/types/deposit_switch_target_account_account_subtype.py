

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DepositSwitchTargetAccountAccountSubtype(enum.StrEnum):
    """
    The account subtype of the account, either `checking` or `savings`.
    """

    CHECKING = "checking"
    SAVINGS = "savings"

    def visit(self, checking: typing.Callable[[], T_Result], savings: typing.Callable[[], T_Result]) -> T_Result:
        if self is DepositSwitchTargetAccountAccountSubtype.CHECKING:
            return checking()
        if self is DepositSwitchTargetAccountAccountSubtype.SAVINGS:
            return savings()
