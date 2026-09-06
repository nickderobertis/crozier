

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class WorkspaceMembershipMethod(enum.StrEnum):
    SSO = "sso"
    DASHBOARD = "dashboard"
    ADMIN = "admin"
    ACCESS_REQUEST = "access_request"

    def visit(
        self,
        sso: typing.Callable[[], T_Result],
        dashboard: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
        access_request: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WorkspaceMembershipMethod.SSO:
            return sso()
        if self is WorkspaceMembershipMethod.DASHBOARD:
            return dashboard()
        if self is WorkspaceMembershipMethod.ADMIN:
            return admin()
        if self is WorkspaceMembershipMethod.ACCESS_REQUEST:
            return access_request()
