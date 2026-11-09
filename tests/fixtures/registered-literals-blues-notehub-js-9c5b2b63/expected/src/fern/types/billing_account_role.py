

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BillingAccountRole(enum.StrEnum):
    BILLING_ADMIN = "billing_admin"
    BILLING_MANAGER = "billing_manager"
    PROJECT_CREATOR = "project_creator"
    BILLING_MEMBER = "billing_member"

    def visit(
        self,
        billing_admin: typing.Callable[[], T_Result],
        billing_manager: typing.Callable[[], T_Result],
        project_creator: typing.Callable[[], T_Result],
        billing_member: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BillingAccountRole.BILLING_ADMIN:
            return billing_admin()
        if self is BillingAccountRole.BILLING_MANAGER:
            return billing_manager()
        if self is BillingAccountRole.PROJECT_CREATOR:
            return project_creator()
        if self is BillingAccountRole.BILLING_MEMBER:
            return billing_member()
