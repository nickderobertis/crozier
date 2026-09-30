

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccessRightOpenAccessRoute(enum.StrEnum):
    GOLD = "gold"
    GREEN = "green"
    HYBRID = "hybrid"
    BRONZE = "bronze"

    def visit(
        self,
        gold: typing.Callable[[], T_Result],
        green: typing.Callable[[], T_Result],
        hybrid: typing.Callable[[], T_Result],
        bronze: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccessRightOpenAccessRoute.GOLD:
            return gold()
        if self is AccessRightOpenAccessRoute.GREEN:
            return green()
        if self is AccessRightOpenAccessRoute.HYBRID:
            return hybrid()
        if self is AccessRightOpenAccessRoute.BRONZE:
            return bronze()
