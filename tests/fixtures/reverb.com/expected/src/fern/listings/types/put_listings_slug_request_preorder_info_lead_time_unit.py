

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutListingsSlugRequestPreorderInfoLeadTimeUnit(enum.StrEnum):
    """
    The unit of time which lead_time is measured in
    """

    DAYS = "days"
    WEEKS = "weeks"

    def visit(self, days: typing.Callable[[], T_Result], weeks: typing.Callable[[], T_Result]) -> T_Result:
        if self is PutListingsSlugRequestPreorderInfoLeadTimeUnit.DAYS:
            return days()
        if self is PutListingsSlugRequestPreorderInfoLeadTimeUnit.WEEKS:
            return weeks()
