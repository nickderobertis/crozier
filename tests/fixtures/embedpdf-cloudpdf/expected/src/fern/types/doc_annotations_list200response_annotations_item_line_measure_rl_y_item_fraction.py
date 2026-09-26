

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlYItemFraction(enum.StrEnum):
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
        if self is DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlYItemFraction.DECIMAL:
            return decimal()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlYItemFraction.FRACTION:
            return fraction()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlYItemFraction.ROUND:
            return round()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlYItemFraction.TRUNCATE:
            return truncate()
