

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IncomeBreakdownType(enum.StrEnum):
    """
    The type of income. Possible values include:
      `"regular"`: regular income
      `"overtime"`: overtime income
      `"bonus"`: bonus income
    """

    BONUS = "bonus"
    OVERTIME = "overtime"
    REGULAR = "regular"

    def visit(
        self,
        bonus: typing.Callable[[], T_Result],
        overtime: typing.Callable[[], T_Result],
        regular: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IncomeBreakdownType.BONUS:
            return bonus()
        if self is IncomeBreakdownType.OVERTIME:
            return overtime()
        if self is IncomeBreakdownType.REGULAR:
            return regular()
