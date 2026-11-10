

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ThemeRulesItemFilterType(enum.StrEnum):
    TYPE = "type"
    API = "api"
    ROLE = "role"

    def visit(
        self,
        type: typing.Callable[[], T_Result],
        api: typing.Callable[[], T_Result],
        role: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ThemeRulesItemFilterType.TYPE:
            return type()
        if self is ThemeRulesItemFilterType.API:
            return api()
        if self is ThemeRulesItemFilterType.ROLE:
            return role()
