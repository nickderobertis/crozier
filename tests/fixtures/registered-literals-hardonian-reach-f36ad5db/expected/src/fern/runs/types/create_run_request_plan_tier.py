

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateRunRequestPlanTier(enum.StrEnum):
    FREE = "free"
    PRO = "pro"
    ENTERPRISE = "enterprise"

    def visit(
        self,
        free: typing.Callable[[], T_Result],
        pro: typing.Callable[[], T_Result],
        enterprise: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateRunRequestPlanTier.FREE:
            return free()
        if self is CreateRunRequestPlanTier.PRO:
            return pro()
        if self is CreateRunRequestPlanTier.ENTERPRISE:
            return enterprise()
