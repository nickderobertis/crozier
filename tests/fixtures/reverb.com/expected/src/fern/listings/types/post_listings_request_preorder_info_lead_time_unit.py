

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostListingsRequestPreorderInfoLeadTimeUnit(str, enum.Enum):
    """
    The unit of time which lead_time is measured in
    """

    DAYS = "days"
    WEEKS = "weeks"

    def visit(self, days: typing.Callable[[], T_Result], weeks: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostListingsRequestPreorderInfoLeadTimeUnit.DAYS:
            return days()
        if self is PostListingsRequestPreorderInfoLeadTimeUnit.WEEKS:
            return weeks()
