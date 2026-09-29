

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class Search1RequestOpenAccessColorItem(enum.StrEnum):
    BRONZE = "bronze"
    GOLD = "gold"
    HYBRID = "hybrid"

    def visit(
        self,
        bronze: typing.Callable[[], T_Result],
        gold: typing.Callable[[], T_Result],
        hybrid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Search1RequestOpenAccessColorItem.BRONZE:
            return bronze()
        if self is Search1RequestOpenAccessColorItem.GOLD:
            return gold()
        if self is Search1RequestOpenAccessColorItem.HYBRID:
            return hybrid()
