

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlAngleItemFraction(enum.StrEnum):
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
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlAngleItemFraction.DECIMAL:
            return decimal()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlAngleItemFraction.FRACTION:
            return fraction()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlAngleItemFraction.ROUND:
            return round()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlAngleItemFraction.TRUNCATE:
            return truncate()
