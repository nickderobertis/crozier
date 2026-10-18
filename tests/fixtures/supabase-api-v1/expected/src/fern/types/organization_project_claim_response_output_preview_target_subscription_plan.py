

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrganizationProjectClaimResponseOutputPreviewTargetSubscriptionPlan(enum.StrEnum):
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
        if self is OrganizationProjectClaimResponseOutputPreviewTargetSubscriptionPlan.FREE:
            return free()
        if self is OrganizationProjectClaimResponseOutputPreviewTargetSubscriptionPlan.PRO:
            return pro()
        if self is OrganizationProjectClaimResponseOutputPreviewTargetSubscriptionPlan.TEAM:
            return team()
        if self is OrganizationProjectClaimResponseOutputPreviewTargetSubscriptionPlan.ENTERPRISE:
            return enterprise()
        if self is OrganizationProjectClaimResponseOutputPreviewTargetSubscriptionPlan.PLATFORM:
            return platform()
