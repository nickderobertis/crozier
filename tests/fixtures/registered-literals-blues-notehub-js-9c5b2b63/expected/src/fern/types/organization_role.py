

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrganizationRole(enum.StrEnum):
    ADMIN = "org_admin"
    BILLING_MANAGER = "billing_manager"
    PROJECT_CREATOR = "project_creator"
    MEMBER = "org_member"

    def visit(
        self,
        admin: typing.Callable[[], T_Result],
        billing_manager: typing.Callable[[], T_Result],
        project_creator: typing.Callable[[], T_Result],
        member: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrganizationRole.ADMIN:
            return admin()
        if self is OrganizationRole.BILLING_MANAGER:
            return billing_manager()
        if self is OrganizationRole.PROJECT_CREATOR:
            return project_creator()
        if self is OrganizationRole.MEMBER:
            return member()
