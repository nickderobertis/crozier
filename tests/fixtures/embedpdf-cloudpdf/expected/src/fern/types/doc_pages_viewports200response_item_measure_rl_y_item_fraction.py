

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocPagesViewports200ResponseItemMeasureRlYItemFraction(enum.StrEnum):
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
        if self is DocPagesViewports200ResponseItemMeasureRlYItemFraction.DECIMAL:
            return decimal()
        if self is DocPagesViewports200ResponseItemMeasureRlYItemFraction.FRACTION:
            return fraction()
        if self is DocPagesViewports200ResponseItemMeasureRlYItemFraction.ROUND:
            return round()
        if self is DocPagesViewports200ResponseItemMeasureRlYItemFraction.TRUNCATE:
            return truncate()
