

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1ProjectsUpdateProjectBudgetRecurrenceItemRecur(enum.StrEnum):
    """
    Recurrence pattern: monthly or until end date
    """

    END_DATE = "end_date"
    MONTH = "month"

    def visit(self, end_date: typing.Callable[[], T_Result], month: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1ProjectsUpdateProjectBudgetRecurrenceItemRecur.END_DATE:
            return end_date()
        if self is V1ProjectsUpdateProjectBudgetRecurrenceItemRecur.MONTH:
            return month()
