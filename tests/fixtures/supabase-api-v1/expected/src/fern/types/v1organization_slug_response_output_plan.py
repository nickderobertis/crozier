

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1OrganizationSlugResponseOutputPlan(enum.StrEnum):
    FREE = "free"
    PRO = "pro"
    TEAM = "team"
    ENTERPRISE = "enterprise"
    PLATFORM = "platform"

    def visit(
        self,
        free: typing.Callable[[], T_Result],
        pro: typing.Callable[[], T_Result],
        team: typing.Callable[[], T_Result],
        enterprise: typing.Callable[[], T_Result],
        platform: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1OrganizationSlugResponseOutputPlan.FREE:
            return free()
        if self is V1OrganizationSlugResponseOutputPlan.PRO:
            return pro()
        if self is V1OrganizationSlugResponseOutputPlan.TEAM:
            return team()
        if self is V1OrganizationSlugResponseOutputPlan.ENTERPRISE:
            return enterprise()
        if self is V1OrganizationSlugResponseOutputPlan.PLATFORM:
            return platform()
