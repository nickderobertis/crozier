

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class DocPagesSetScaleRequestMeasureAreaItemFraction(enum.StrEnum):
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
        if self is DocPagesSetScaleRequestMeasureAreaItemFraction.DECIMAL:
            return decimal()
        if self is DocPagesSetScaleRequestMeasureAreaItemFraction.FRACTION:
            return fraction()
        if self is DocPagesSetScaleRequestMeasureAreaItemFraction.ROUND:
            return round()
        if self is DocPagesSetScaleRequestMeasureAreaItemFraction.TRUNCATE:
            return truncate()
