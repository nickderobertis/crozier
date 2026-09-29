

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GraphResultOpenAccessColor(enum.StrEnum):
    GOLD = "gold"
    HYBRID = "hybrid"
    BRONZE = "bronze"

    def visit(
        self,
        gold: typing.Callable[[], T_Result],
        hybrid: typing.Callable[[], T_Result],
        bronze: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GraphResultOpenAccessColor.GOLD:
            return gold()
        if self is GraphResultOpenAccessColor.HYBRID:
            return hybrid()
        if self is GraphResultOpenAccessColor.BRONZE:
            return bronze()
