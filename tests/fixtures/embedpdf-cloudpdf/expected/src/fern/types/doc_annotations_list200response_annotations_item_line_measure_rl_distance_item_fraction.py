

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlDistanceItemFraction(enum.StrEnum):
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
        if self is DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlDistanceItemFraction.DECIMAL:
            return decimal()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlDistanceItemFraction.FRACTION:
            return fraction()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlDistanceItemFraction.ROUND:
            return round()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlDistanceItemFraction.TRUNCATE:
            return truncate()
