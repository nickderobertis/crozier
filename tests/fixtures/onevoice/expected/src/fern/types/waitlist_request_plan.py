

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WaitlistRequestPlan(enum.StrEnum):
    """
    Optional requested plan; omitted values preserve existing interest.
    """

    PRO = "pro"

    def visit(self, pro: typing.Callable[[], T_Result]) -> T_Result:
        if self is WaitlistRequestPlan.PRO:
            return pro()
