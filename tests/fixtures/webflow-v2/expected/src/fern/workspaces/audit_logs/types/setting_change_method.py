

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class SettingChangeMethod(enum.StrEnum):
    DASHBOARD = "dashboard"
    ADMIN = "admin"

    def visit(self, dashboard: typing.Callable[[], T_Result], admin: typing.Callable[[], T_Result]) -> T_Result:
        if self is SettingChangeMethod.DASHBOARD:
            return dashboard()
        if self is SettingChangeMethod.ADMIN:
            return admin()
