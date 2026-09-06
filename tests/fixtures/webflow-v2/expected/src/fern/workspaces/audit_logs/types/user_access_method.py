

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class UserAccessMethod(enum.StrEnum):
    DASHBOARD = "dashboard"
    SSO = "sso"
    API = "api"
    GOOGLE = "google"

    def visit(
        self,
        dashboard: typing.Callable[[], T_Result],
        sso: typing.Callable[[], T_Result],
        api: typing.Callable[[], T_Result],
        google: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UserAccessMethod.DASHBOARD:
            return dashboard()
        if self is UserAccessMethod.SSO:
            return sso()
        if self is UserAccessMethod.API:
            return api()
        if self is UserAccessMethod.GOOGLE:
            return google()
