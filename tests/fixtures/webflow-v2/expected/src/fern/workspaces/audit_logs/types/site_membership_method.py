

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class SiteMembershipMethod(enum.StrEnum):
    SSO = "sso"
    INVITE = "invite"
    SCIM = "scim"
    DASHBOARD = "dashboard"
    ADMIN = "admin"
    ACCESS_REQUEST = "access_request"

    def visit(
        self,
        sso: typing.Callable[[], T_Result],
        invite: typing.Callable[[], T_Result],
        scim: typing.Callable[[], T_Result],
        dashboard: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
        access_request: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SiteMembershipMethod.SSO:
            return sso()
        if self is SiteMembershipMethod.INVITE:
            return invite()
        if self is SiteMembershipMethod.SCIM:
            return scim()
        if self is SiteMembershipMethod.DASHBOARD:
            return dashboard()
        if self is SiteMembershipMethod.ADMIN:
            return admin()
        if self is SiteMembershipMethod.ACCESS_REQUEST:
            return access_request()
