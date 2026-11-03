

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class IssuePassRequestGrant(enum.StrEnum):
    DAY_VISIT = "day-visit"
    OVERNIGHT_STAY = "overnight-stay"

    def visit(
        self, day_visit: typing.Callable[[], T_Result], overnight_stay: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is IssuePassRequestGrant.DAY_VISIT:
            return day_visit()
        if self is IssuePassRequestGrant.OVERNIGHT_STAY:
            return overnight_stay()
