

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrganizationProjectClaimResponseOutputPreviewSourceSubscriptionPlan(enum.StrEnum):
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
        if self is OrganizationProjectClaimResponseOutputPreviewSourceSubscriptionPlan.FREE:
            return free()
        if self is OrganizationProjectClaimResponseOutputPreviewSourceSubscriptionPlan.PRO:
            return pro()
        if self is OrganizationProjectClaimResponseOutputPreviewSourceSubscriptionPlan.TEAM:
            return team()
        if self is OrganizationProjectClaimResponseOutputPreviewSourceSubscriptionPlan.ENTERPRISE:
            return enterprise()
        if self is OrganizationProjectClaimResponseOutputPreviewSourceSubscriptionPlan.PLATFORM:
            return platform()
