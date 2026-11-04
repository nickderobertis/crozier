

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ReviewListMineResponseItemChipsetVariant(enum.StrEnum):
    BASE = "BASE"
    PRO = "PRO"
    MAX = "MAX"
    ULTRA = "ULTRA"

    def visit(
        self,
        base: typing.Callable[[], T_Result],
        pro: typing.Callable[[], T_Result],
        max: typing.Callable[[], T_Result],
        ultra: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReviewListMineResponseItemChipsetVariant.BASE:
            return base()
        if self is ReviewListMineResponseItemChipsetVariant.PRO:
            return pro()
        if self is ReviewListMineResponseItemChipsetVariant.MAX:
            return max()
        if self is ReviewListMineResponseItemChipsetVariant.ULTRA:
            return ultra()
