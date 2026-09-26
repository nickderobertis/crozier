

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlAngleItemFraction(enum.StrEnum):
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
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlAngleItemFraction.DECIMAL:
            return decimal()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlAngleItemFraction.FRACTION:
            return fraction()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlAngleItemFraction.ROUND:
            return round()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlAngleItemFraction.TRUNCATE:
            return truncate()
