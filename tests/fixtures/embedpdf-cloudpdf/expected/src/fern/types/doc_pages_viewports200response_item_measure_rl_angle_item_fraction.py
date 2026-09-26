

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocPagesViewports200ResponseItemMeasureRlAngleItemFraction(enum.StrEnum):
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
        if self is DocPagesViewports200ResponseItemMeasureRlAngleItemFraction.DECIMAL:
            return decimal()
        if self is DocPagesViewports200ResponseItemMeasureRlAngleItemFraction.FRACTION:
            return fraction()
        if self is DocPagesViewports200ResponseItemMeasureRlAngleItemFraction.ROUND:
            return round()
        if self is DocPagesViewports200ResponseItemMeasureRlAngleItemFraction.TRUNCATE:
            return truncate()
