

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchRequestOpenAccessColorItem(enum.StrEnum):
    BRONZE = "bronze"
    GOLD = "gold"
    HYBRID = "hybrid"

    def visit(
        self,
        bronze: typing.Callable[[], T_Result],
        gold: typing.Callable[[], T_Result],
        hybrid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchRequestOpenAccessColorItem.BRONZE:
            return bronze()
        if self is SearchRequestOpenAccessColorItem.GOLD:
            return gold()
        if self is SearchRequestOpenAccessColorItem.HYBRID:
            return hybrid()
