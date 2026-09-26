

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocPagesViewports200ResponseItemMeasureRlDistanceItemFraction(enum.StrEnum):
    DECIMAL = "decimal"
    FRACTION = "fraction"
    ROUND = "round"
    TRUNCATE = "truncate"

    def visit(
        self,
        decimal: typing.Callable[[], T_Result],
        fraction: typing.Callable[[], T_Result],
        round: typing.Callable[[], T_Result],
        truncate: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocPagesViewports200ResponseItemMeasureRlDistanceItemFraction.DECIMAL:
            return decimal()
        if self is DocPagesViewports200ResponseItemMeasureRlDistanceItemFraction.FRACTION:
            return fraction()
        if self is DocPagesViewports200ResponseItemMeasureRlDistanceItemFraction.ROUND:
            return round()
        if self is DocPagesViewports200ResponseItemMeasureRlDistanceItemFraction.TRUNCATE:
            return truncate()
