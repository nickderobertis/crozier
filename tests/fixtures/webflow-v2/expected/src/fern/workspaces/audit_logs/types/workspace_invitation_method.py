

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class WorkspaceInvitationMethod(enum.StrEnum):
    SSO = "sso"
    DASHBOARD = "dashboard"
    ADMIN = "admin"

    def visit(
        self,
        sso: typing.Callable[[], T_Result],
        dashboard: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WorkspaceInvitationMethod.SSO:
            return sso()
        if self is WorkspaceInvitationMethod.DASHBOARD:
            return dashboard()
        if self is WorkspaceInvitationMethod.ADMIN:
            return admin()
