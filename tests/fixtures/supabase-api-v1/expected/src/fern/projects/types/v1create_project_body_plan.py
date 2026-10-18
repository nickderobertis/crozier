

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1CreateProjectBodyPlan(enum.StrEnum):
    """
    Subscription Plan is now set on organization level and is ignored in this request
    """

    FREE = "free"
    PRO = "pro"

    def visit(self, free: typing.Callable[[], T_Result], pro: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1CreateProjectBodyPlan.FREE:
            return free()
        if self is V1CreateProjectBodyPlan.PRO:
            return pro()
