

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class DocPagesSetScaleRequestMeasureAngleItemFraction(enum.StrEnum):
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
        if self is DocPagesSetScaleRequestMeasureAngleItemFraction.DECIMAL:
            return decimal()
        if self is DocPagesSetScaleRequestMeasureAngleItemFraction.FRACTION:
            return fraction()
        if self is DocPagesSetScaleRequestMeasureAngleItemFraction.ROUND:
            return round()
        if self is DocPagesSetScaleRequestMeasureAngleItemFraction.TRUNCATE:
            return truncate()
