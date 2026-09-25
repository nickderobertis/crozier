

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1ProjectsUpdateProjectBudgetRecurrenceItemRecurUntil(enum.StrEnum):
    """
    When to stop recurring: until end date or until project is archived
    """

    END_DATE = "end_date"
    ARCHIVED = "archived"

    def visit(self, end_date: typing.Callable[[], T_Result], archived: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1ProjectsUpdateProjectBudgetRecurrenceItemRecurUntil.END_DATE:
            return end_date()
        if self is V1ProjectsUpdateProjectBudgetRecurrenceItemRecurUntil.ARCHIVED:
            return archived()
