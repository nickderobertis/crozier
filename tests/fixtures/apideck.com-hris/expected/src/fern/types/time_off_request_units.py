

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TimeOffRequestUnits(str, enum.Enum):
    """
    The unit of time off requested. Possible values include: `hours`, `days`, or `other`.
    """

    DAYS = "days"
    HOURS = "hours"
    OTHER = "other"

    def visit(
        self,
        days: typing.Callable[[], T_Result],
        hours: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TimeOffRequestUnits.DAYS:
            return days()
        if self is TimeOffRequestUnits.HOURS:
            return hours()
        if self is TimeOffRequestUnits.OTHER:
            return other()
